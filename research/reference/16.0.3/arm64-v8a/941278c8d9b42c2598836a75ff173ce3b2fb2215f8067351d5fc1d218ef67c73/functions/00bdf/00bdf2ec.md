# 00bdf2ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdf2ec",
  "name": "_ZN8firebase4auth4UserD2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a10af5a179236e6719a8c7bd5cdad893733a77809ad6b3d76b89b4e9c4567df4",
  "source_text_sha256": "a10af5a179236e6719a8c7bd5cdad893733a77809ad6b3d76b89b4e9c4567df4"
}
~~~

## 呼び出し元

- [00c5baf0](../00c5b/00c5baf0.md)

## 呼び出し先

- [00c5ec20](../00c5e/00c5ec20.md)

## 疑似コード / UTF-8 242 bytes

~~~c

void _ZN8firebase4auth4UserD2Ev(long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9ca60;
  param_1[0x13] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN8firebase4auth17UserInfoInterfaceD2Ev();
  return;
}

~~~
