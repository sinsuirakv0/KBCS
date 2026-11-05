# 00adffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adffcc.md)

## 関数情報

~~~json
{
  "address": "00adffcc",
  "name": "_ZN8firebase9analytics8internal10FutureData6CreateEv",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f385d5590ca7ae3624e2de878dd834457927e0f9034fb6a83cedf70062e0faa1",
  "source_text_sha256": "f385d5590ca7ae3624e2de878dd834457927e0f9034fb6a83cedf70062e0faa1"
}
~~~
## 呼び出し元

- [00bddd60](../00bdd/00bddd60.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddce0](../00bdd/00bddce0.md)

## 疑似コード 1/1 / UTF-8 297 bytes

~~~c

undefined8 _ZN8firebase9analytics8internal10FutureData6CreateEv(void)

{
  undefined8 uVar1;
  
  uVar1 = _Znwm(0x130);
  _ZN8firebase26ReferenceCountedFutureImplC2Em(uVar1,2);
  *(undefined8 *)PTR__ZN8firebase9analytics8internal10FutureData14s_future_data_E_00c1b7a0 = uVar1;
  return uVar1;
}

~~~
