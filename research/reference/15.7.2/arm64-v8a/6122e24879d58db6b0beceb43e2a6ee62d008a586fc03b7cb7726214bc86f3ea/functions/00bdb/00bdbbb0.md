# 00bdbbb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbbb0.md)

## 関数情報

~~~json
{
  "address": "00bdbbb0",
  "name": "Botan::Internal_Error::Internal_Error",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41ebb362021388bc660bd51ad52658b8506d401d1a77caacfc9467e6a11ce8a5",
  "source_text_sha256": "41ebb362021388bc660bd51ad52658b8506d401d1a77caacfc9467e6a11ce8a5"
}
~~~
## 呼び出し元

- [0048fc00](../0048f/0048fc00.md)
- [00493850](../00493/00493850.md)
- [004bb3f0](../004bb/004bb3f0.md)
- [004bb59c](../004bb/004bb59c.md)
- [004bb70c](../004bb/004bb70c.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004cd86c](../004cd/004cd86c.md)
- [004fc6ac](../004fc/004fc6ac.md)

## 呼び出し先

- [004d7c34](../004d7/004d7c34.md)

## 疑似コード 1/1 / UTF-8 167 bytes

~~~c

void __thiscall Botan::Internal_Error::Internal_Error(Internal_Error *this,basic_string *param_1)

{
  (*(code *)PTR_Internal_Error_00c1c610)();
  return;
}

~~~
