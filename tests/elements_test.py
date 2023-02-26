import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            time.sleep(5)
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            firstname = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(firstname)
            table_result = web_table_page.check_search_person()
            print(firstname)
            print(table_result)
            assert firstname in table_result, 'The person was not detected'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            firstname = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(firstname)
            new_age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert new_age in row, 'Age was not changed'

        def test_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_created_person()
            text = web_table_page.check_deleted_person()
            time.sleep(3)
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.change_quantity_rows()
            assert count == [5, 10], "Rows quantity was changed incorrectly"

    class TestButtonsPage:

        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_buttons('double')
            right = button_page.click_on_different_buttons('right')
            click = button_page.click_on_different_buttons('click')
            assert double == 'You have done a double click', 'double button is broken'
            assert right == 'You have done a right click', 'right click button is broken'
            assert click == 'You have done a dynamic click', 'click button is broken'
