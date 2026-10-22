# 00bdcbc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcbc0.md)

## 関数情報

~~~json
{
  "address": "00bdcbc0",
  "name": "Botan::AlternativeName::AlternativeName",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8f53121ee6e533a98c3945f8dad46b4e956950846ff612c1d2774a3957a2a1e",
  "source_text_sha256": "b8f53121ee6e533a98c3945f8dad46b4e956950846ff612c1d2774a3957a2a1e"
}
~~~
## 呼び出し元

- [004e21a8](../004e2/004e21a8.md)
- [004f27ec](../004f2/004f27ec.md)
- [004fb978](../004fb/004fb978.md)
- [0050a638](../0050a/0050a638.md)
- [0050af44](../0050a/0050af44.md)
- [0050b45c](../0050b/0050b45c.md)
- [005185dc](../00518/005185dc.md)
- [0051a694](../0051a/0051a694.md)
- [0051ac6c](../0051a/0051ac6c.md)

## 呼び出し先

- [004dbf98](../004db/004dbf98.md)

## 疑似コード 1/1 / UTF-8 690 bytes

~~~c

void __thiscall
Botan::AlternativeName::AlternativeName
          (AlternativeName *this,basic_string *param_1,basic_string *param_2,basic_string *param_3,
          basic_string *param_4)

{
                    /* catch() { ... } // from try @ 00bdccc0 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcde0 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdce58 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcf2c with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcfb0 with catch @ 00bdcbcc */
  (*(code *)PTR_AlternativeName_00c1ce18)();
  return;
}

~~~
