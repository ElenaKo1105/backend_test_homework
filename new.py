WTF where is my files git 
# ...backend_test_homework/
**
# Добавить новые и изменённые файлы в индекс.
git add . 
# Зафиксировать изменения.
git commit -m "Add new file"
# Отправить изменения в удалённый репозиторий.
git push  


# Удаляем файл из отслеживания, но не удаляем из папки на компьютере.
git rm --cached new.py
# Фиксируем изменения в локальном репозитории.
git commit -m "Delete new file"
# Отправляем изменения в удалённый репозиторий.
git push 