import os
from selene import be, have, browser, command


def test_registration(browser_setting):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Julia')
    browser.element('#lastName').should(be.blank).type('Loginova')
    browser.element('#userEmail').should(be.blank).type('badhumster@test.ru')
    browser.element('[for="gender-radio-2"]').should(be.visible).click()
    browser.element('#userNumber').should(be.blank).type('8922900123')
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element('.react-datepicker__month-select').should(be.clickable).click()
    browser.element('[value="9"]').should(be.clickable).click()
    browser.element('.react-datepicker__year-select').should(be.clickable).click()
    browser.element('[value="1995"]').should(be.clickable).click()
    browser.element('div[class="react-datepicker__day react-datepicker__day--011"]').should(be.clickable).click()
    browser.element('#subjectsInput').should(be.blank).type('Com').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/bunny.jpeg')
    browser.element("#currentAddress").should(be.blank).type('Yerevan')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('#react-select-3-input').should(be.blank).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Noida').press_enter().press_enter()

    # Чек на заполнение

    browser.element('//tbody/tr[1]/td[2]').should(have.text('Julia Loginova'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('badhumster@test.ru'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Female'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('8922900123'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('11 October,1995'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Computer Science'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Music'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('bunny.jpeg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('Yerevan'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('NCR Noida'))
