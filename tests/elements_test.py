import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the cur_add does not match"
            assert permanent_address == output_per_addr, "the per_add does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_output_result()   # I could not find the elements so did like this for now
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Error"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_random_radio_button('Yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_random_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_random_radio_button('No')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', '"yes" was not selected'
            assert output_impressive == 'Impressive', '"impressive" was not selected'
            assert output_no == 'No', '"no" was not selected'







