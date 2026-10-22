# 00bdbaa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbaa0.md)

## 関数情報

~~~json
{
  "address": "00bdbaa0",
  "name": "std::__ndk1::stoul",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68befe6456bc6b3a85f9b100487d3bf174696ac704f09a4218deace169a942de",
  "source_text_sha256": "68befe6456bc6b3a85f9b100487d3bf174696ac704f09a4218deace169a942de"
}
~~~
## 呼び出し元

- [0048bf84](../0048b/0048bf84.md)

## 呼び出し先

- [00b77e98](../00b77/00b77e98.md)

## 疑似コード 1/1 / UTF-8 157 bytes

~~~c

void std::__ndk1::stoul(basic_string *param_1,ulong *param_2,int param_3)

{
  (*(code *)PTR_stoul_00c1c588)(param_1,param_2,param_3);
  return;
}

~~~
