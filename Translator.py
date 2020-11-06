from translate import Translator

translator = Translator(from_lang='chinese',to_lang='english')
value = translator.translate("我只喜欢你")
print(value)
value2 = translator.translate("对就是你")
print(value2)
