# 00bdbbd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbbd0.md)

## 関数情報

~~~json
{
  "address": "00bdbbd0",
  "name": "Botan::BigInt::cmp",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a782931810e08558f7de802d950cc43779a16e11d5853da85ed5d7836170f06c",
  "source_text_sha256": "a782931810e08558f7de802d950cc43779a16e11d5853da85ed5d7836170f06c"
}
~~~
## 呼び出し元

- [0048ff2c](../0048f/0048ff2c.md)
- [00493850](../00493/00493850.md)
- [00495378](../00495/00495378.md)
- [004967a4](../00496/004967a4.md)
- [00497bf4](../00497/00497bf4.md)
- [004b5c14](../004b5/004b5c14.md)
- [004b6640](../004b6/004b6640.md)
- [004b6d50](../004b6/004b6d50.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb928](../004bb/004bb928.md)
- [004bbdd8](../004bb/004bbdd8.md)
- [004bcf24](../004bc/004bcf24.md)
- [004bdd7c](../004bd/004bdd7c.md)
- [004be0f4](../004be/004be0f4.md)
- [004cf4d8](../004cf/004cf4d8.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [004d1904](../004d1/004d1904.md)
- [004e939c](../004e9/004e939c.md)
- [00513fc4](../00513/00513fc4.md)
- [00514cc0](../00514/00514cc0.md)
- [00516464](../00516/00516464.md)
- [005168d8](../00516/005168d8.md)

## 呼び出し先

- [00498160](../00498/00498160.md)

## 疑似コード 1/1 / UTF-8 156 bytes

~~~c

void __thiscall Botan::BigInt::cmp(BigInt *this,BigInt *param_1,bool param_2)

{
  (*(code *)PTR_cmp_00c1c620)(this,param_1,param_2);
  return;
}

~~~
