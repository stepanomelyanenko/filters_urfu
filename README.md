На основании предыдущего проекта сделайте свой репозиторий на GitHub. Поместите туда ваш новый файл filter.py, также в репозиторий поместите первоначальный файл filter.py (old_filter.py).
Создайте новый проект. Подключите ваш репозиторий к IDE PyCharm. Загрузите оба файла с помощью Git в PyCharm к себе в проект на компьютер.
Добавьте в папку с вашим проектом тестовое изображение, из которого будете получать готовое изображение с фильтром.
Добавьте файл в репозиторий и отправьте его на сервер. Предполагаем, что ваш новый filter.py работает как утилита, где нужно указать во время выполнения имя файла для конвертирования, а также размер блока, и количество градаций серого (также в нем все разделено на необходимые функции и используются все преобразования с матрицами с помощью библиотеки numpy).
Запустите с помощью встроенного профилизатора в PyCharm ваш новый filter.py, сделайте скриншот со временем выполнения.
Также запустите в профилизаторе old_filter.py. Посмотрите разницу во времени выполнения кода. Полученные скриншоты со временем выполнения с объяснением результатов поместите в файл README.MD
Поскольку в вашем файле большая часть времени выполнения затрачивается на ввод данных пользователем, поэтому создайте копию вашего файла filter_with_filename.py, добавьте его также в репозиторий, в котором сразу в код введите имя изображения для конвертирования, а также аналогичные параметры для конвертирования, которые указаны были в первоначальном old_filter.py, а именно размер блока 10 и 50 градаций серого. Также закомитьте полученные правки и отправьте их на сервер.
Запустите в профилизаторе файл filter_with_filename.py, сделайте скриншот со временем выполнения этого файла. Полученный скриншот, а также объяснение полученных результатов добавьте в файл README.MD. Также в файл README.MD с помощью wiki-разметки добавьте все изображения до преобразования и после.
![image](https://user-images.githubusercontent.com/71918545/143187112-7f81d038-b0de-4c81-900a-87d28dfac1c7.png)
![image](https://user-images.githubusercontent.com/71918545/143187134-24146965-297d-4bff-9f3b-1953658fff2c.png)
К выделенным функциям, допишите документацию и doc-тесты в формате: docstring.
Проверьте запуск doc-тестов в PyCharm. Сделайте их скриншоты.
Закомитьте все изменения на github. Скриншоты doc-тесты с соответствующими комментариями прикрепите в файл README.MD.
Проинспектируйте ваш проект в PyCharm. Исправьте все замечания по PEP8. Закомитьте в репозиторий с соответствующей подписью в коммите.
Через отладчик вывести на экран в свойствах изображения ширину и высоту, а также тип изображения. Также в отладчике выведите значения ширины блока и количество градаций серого.
Сделайте скриншоты результата работы отладчика и вставьте их в файл README.MD.

