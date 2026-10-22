# 00bddbb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddbb0.md)

## 関数情報

~~~json
{
  "address": "00bddbb0",
  "name": "firebase::Variant::assert_is_type",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "80bcc9f63acae8176f20e01a0dbd5fb14cb40f0b31689d245bef6878625c7bb5",
  "source_text_sha256": "80bcc9f63acae8176f20e01a0dbd5fb14cb40f0b31689d245bef6878625c7bb5"
}
~~~
## 呼び出し元

- [0084a918](../0084a/0084a918.md)
- [00ae1a54](../00ae1/00ae1a54.md)
- [00ae1d14](../00ae1/00ae1d14.md)
- [00af18f4](../00af1/00af18f4.md)
- [00b5732c](../00b57/00b5732c.md)

## 呼び出し先

- [00b04448](../00b04/00b04448.md)

## 疑似コード 1/1 / UTF-8 125 bytes

~~~c

void __thiscall firebase::Variant::assert_is_type(void)

{
  (*(code *)PTR_assert_is_type_00c1d610)();
  return;
}

~~~
