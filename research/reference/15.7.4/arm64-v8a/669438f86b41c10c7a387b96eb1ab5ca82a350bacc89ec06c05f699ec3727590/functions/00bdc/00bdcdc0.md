# 00bdcdc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZNK5Botan16X509_Certificate23load_subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552",
  "source_text_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552"
}
~~~

## 呼び出し元

- [004e85ec](../004e8/004e85ec.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [00500f10](../00500/00500f10.md)

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNK5Botan16X509_Certificate23load_subject_public_keyEv(void)

{
                    /* try { // try from 00bdcdcc to 00cdced3 has its CatchHandler @ 00bdccd8 */
  (*(code *)PTR__ZNK5Botan16X509_Certificate23load_subject_public_keyEv_00c1cf98)();
  return;
}

~~~
