# 00bdbfc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbfc0.md)

## 関数情報

~~~json
{
  "address": "00bdbfc0",
  "name": "std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::open",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "34719a60f9bb65af0cffcf72b08a9955863efc4c33b08e4f89ba34912f03bb70",
  "source_text_sha256": "34719a60f9bb65af0cffcf72b08a9955863efc4c33b08e4f89ba34912f03bb70"
}
~~~
## 呼び出し元

- [004a36fc](../004a3/004a36fc.md)
- [004d7338](../004d7/004d7338.md)
- [00b46650](../00b46/00b46650.md)
- [00b46e18](../00b46/00b46e18.md)

## 呼び出し先

- [00b48960](../00b48/00b48960.md)

## 疑似コード 1/1 / UTF-8 263 bytes

~~~c

void __thiscall
std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::open
          (basic_filebuf<char,std::__ndk1::char_traits<char>> *this,char *param_1,uint param_2)

{
  (*(code *)PTR_open_00c1c818)(this,param_1,param_2);
  return;
}

~~~
