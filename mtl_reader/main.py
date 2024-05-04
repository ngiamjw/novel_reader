import folder_maker as fm
import chapter_text as ct
from chapter_text import chapter_texts as ct
import chapter_links as cl
import test

folder_path = fm.folder_maker(cl.novel_name())


for i in cl.chapter_list():
    chapter = ct(i)
    text = "".join(chapter.novel_content())
    edited_text = test.editor(text)
    chapter_number = chapter.chapter_number()
    file_path = fm.file_maker(chapter_number, folder_path)

    with open(file_path, 'w', encoding='utf-8') as fn:
        fn.write("".join(text))
