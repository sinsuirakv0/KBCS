# 00baef1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baef1c.md)

## 関数情報

~~~json
{
  "address": "00baef1c",
  "name": "std::__ndk1::numpunct<wchar_t>::numpunct",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe5344a68a432975eefdfb2852f9f293253ce3d4d019da90b063d33a526e000f",
  "source_text_sha256": "fe5344a68a432975eefdfb2852f9f293253ce3d4d019da90b063d33a526e000f"
}
~~~
## 呼び出し元

- [00be1720](../00be1/00be1720.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 521 bytes

~~~c

/* std::__ndk1::numpunct<wchar_t>::numpunct(unsigned long) */

void __thiscall std::__ndk1::numpunct<wchar_t>::numpunct(numpunct<wchar_t> *this,ulong param_1)

{
  undefined8 uVar1;
  undefined *puVar2;
  
  puVar2 = PTR_vtable_00c1bec0;
  uVar1 = DAT_002b2b98;
  *(undefined8 *)(this + 0x20) = 0;
  *(undefined8 *)(this + 0x28) = 0;
  *(undefined8 *)(this + 0x18) = 0;
  *(undefined8 *)(this + 0x10) = uVar1;
  *(undefined **)this = puVar2 + 0x10;
  *(ulong *)(this + 8) = param_1 - 1;
  return;
}

~~~
