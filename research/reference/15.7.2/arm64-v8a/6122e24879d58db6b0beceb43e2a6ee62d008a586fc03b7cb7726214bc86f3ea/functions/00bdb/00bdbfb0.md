# 00bdbfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbfb0.md)

## 関数情報

~~~json
{
  "address": "00bdbfb0",
  "name": "std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::basic_filebuf",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3123f1cb210894517303886c19a57d3a00a1f23027aaf24b19306c86d4c54bc5",
  "source_text_sha256": "3123f1cb210894517303886c19a57d3a00a1f23027aaf24b19306c86d4c54bc5"
}
~~~
## 呼び出し元

- [004a36fc](../004a3/004a36fc.md)
- [004d7338](../004d7/004d7338.md)

## 呼び出し先

- [00b88710](../00b88/00b88710.md)

## 疑似コード 1/1 / UTF-8 234 bytes

~~~c

void __thiscall
std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::basic_filebuf
          (basic_filebuf<char,std::__ndk1::char_traits<char>> *this)

{
  (*(code *)PTR_basic_filebuf_00c1c810)();
  return;
}

~~~
