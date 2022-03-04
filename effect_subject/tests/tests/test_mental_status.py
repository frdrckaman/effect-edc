from django.test import TestCase, tag
from edc_constants.constants import NO, NOT_APPLICABLE, YES
from edc_visit_schedule.constants import DAY1
from model_bakery import baker

from effect_screening.tests.effect_test_case_mixin import EffectTestCaseMixin
from effect_subject.forms import MentalStatusForm
from effect_subject.forms.mental_status_form import MentalStatusFormValidator
from effect_visit_schedule.constants import DAY14


@tag("ms")
class TestMentalStatus(EffectTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_visit = self.get_subject_visit()

    def test_ok(self):
        subject_visit = self.subject_visit
        obj = baker.make_recipe(
            "effect_subject.mentalstatus", subject_visit=subject_visit
        )
        form = MentalStatusForm(instance=obj)
        form.is_valid()


@tag("ms")
class TestMentalStatusFormValidation(EffectTestCaseMixin, TestCase):

    form_validator_default_form_cls = MentalStatusFormValidator

    def setUp(self):
        super().setUp()
        self.subject_visit = self.get_subject_visit()

    def get_valid_mental_status_data(self, visit_code: str = DAY1):
        self.subject_visit.appointment.visit_code = visit_code
        return {
            "subject_visit": self.subject_visit,
            "appointment": self.subject_visit.appointment,
            "report_datetime": self.subject_visit.report_datetime,
            "recent_seizure": NO,
            "behaviour_change": NO,
            "confusion": NO,
            "modified_rankin_score": "0",
            "ecog_score": "0",
            "glasgow_coma_score": 15,
            "reportable_as_ae": NOT_APPLICABLE if visit_code == DAY1 else NO,
            "patient_admitted": NOT_APPLICABLE if visit_code == DAY1 else NO,
        }

    def test_valid_mental_status_data_valid_baseline(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY1)
        self.assertFormValidatorNoError(
            form_validator=self.validate_form_validator(cleaned_data)
        )

    def test_valid_mental_status_data_valid_d14(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY14)
        self.assertFormValidatorNoError(
            form_validator=self.validate_form_validator(cleaned_data)
        )

    def test_reportable_as_ae_not_applicable_at_baseline(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY1)
        for response in [YES, NO]:
            with self.subTest(reportable_as_ae=response):
                cleaned_data.update({"reportable_as_ae": response})
                self.assertFormValidatorError(
                    field="reportable_as_ae",
                    expected_msg=(
                        "This field is not applicable. Expected 'Not applicable' at baseline."
                    ),
                    form_validator=self.validate_form_validator(cleaned_data),
                )

    def test_patient_admitted_not_applicable_at_baseline(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY1)
        for response in [YES, NO]:
            with self.subTest(patient_admitted=response):
                cleaned_data.update({"patient_admitted": response})
                self.assertFormValidatorError(
                    field="patient_admitted",
                    expected_msg=(
                        "This field is not applicable. Expected 'Not applicable' at baseline."
                    ),
                    form_validator=self.validate_form_validator(cleaned_data),
                )

    def test_reportable_as_ae_applicable_at_d14(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY14)
        cleaned_data.update({"reportable_as_ae": NOT_APPLICABLE})
        self.assertFormValidatorError(
            field="reportable_as_ae",
            expected_msg="This field is applicable.",
            form_validator=self.validate_form_validator(cleaned_data),
        )
        for response in [YES, NO]:
            with self.subTest(reportable_as_ae=response):
                cleaned_data.update({"reportable_as_ae": response})
                self.assertFormValidatorNoError(
                    form_validator=self.validate_form_validator(cleaned_data)
                )

    def test_patient_admitted_applicable_at_d14(self):
        cleaned_data = self.get_valid_mental_status_data(visit_code=DAY14)
        cleaned_data.update({"patient_admitted": NOT_APPLICABLE})
        self.assertFormValidatorError(
            field="patient_admitted",
            expected_msg="This field is applicable.",
            form_validator=self.validate_form_validator(cleaned_data),
        )
        for response in [YES, NO]:
            with self.subTest(patient_admitted=response):
                cleaned_data.update({"patient_admitted": response})
                self.assertFormValidatorNoError(
                    form_validator=self.validate_form_validator(cleaned_data)
                )
