# 00baeef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baeef0.md)

## 関数情報

~~~json
{
  "address": "00baeef0",
  "name": "std::__ndk1::numpunct<char>::numpunct",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a425b927916dfac48ca0337009182e14a54d4174d9849ced7bda938bf1c93454",
  "source_text_sha256": "a425b927916dfac48ca0337009182e14a54d4174d9849ced7bda938bf1c93454"
}
~~~
## 呼び出し元

- [00be1710](../00be1/00be1710.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 467 bytes

~~~c

/* std::__ndk1::numpunct<char>::numpunct(unsigned long) */

void __thiscall std::__ndk1::numpunct<char>::numpunct(numpunct<char> *this,ulong param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR_vtable_00c1beb8;
  *(undefined2 *)(this + 0x10) = 0x2c2e;
  *(undefined8 *)(this + 0x20) = 0;
  *(undefined8 *)(this + 0x28) = 0;
  *(undefined8 *)(this + 0x18) = 0;
  *(undefined **)this = puVar1 + 0x10;
  *(ulong *)(this + 8) = param_1 - 1;
  return;
}

~~~
