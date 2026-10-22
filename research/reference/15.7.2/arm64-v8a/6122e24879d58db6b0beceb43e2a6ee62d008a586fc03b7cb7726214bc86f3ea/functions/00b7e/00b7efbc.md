# 00b7efbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7efbc.md)

## 関数情報

~~~json
{
  "address": "00b7efbc",
  "name": "std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::operator=",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab5f7d06551cf495bfa8389be991fe1dd88bdf60a0bec4ba9bca38d078bebe57",
  "source_text_sha256": "ab5f7d06551cf495bfa8389be991fe1dd88bdf60a0bec4ba9bca38d078bebe57"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be11e0](../00be1/00be11e0.md)

## 疑似コード 1/1 / UTF-8 1006 bytes

~~~c

/* std::__ndk1::basic_streambuf<char, std::__ndk1::char_traits<char>
   >::TEMPNAMEPLACEHOLDERVALUE(std::__ndk1::basic_streambuf<char, std::__ndk1::char_traits<char> >
   const&) */

basic_streambuf<char,std::__ndk1::char_traits<char>> * __thiscall
std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::operator=
          (basic_streambuf<char,std::__ndk1::char_traits<char>> *this,basic_streambuf *param_1)

{
  undefined8 uVar1;
  
  locale::operator=((locale *)(this + 8),(locale *)(param_1 + 8));
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *(undefined8 *)(this + 0x18) = *(undefined8 *)(param_1 + 0x18);
  *(undefined8 *)(this + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x20);
  *(undefined8 *)(this + 0x28) = *(undefined8 *)(param_1 + 0x28);
  *(undefined8 *)(this + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(this + 0x38) = *(undefined8 *)(param_1 + 0x38);
  *(undefined8 *)(this + 0x30) = uVar1;
  return this;
}

~~~
