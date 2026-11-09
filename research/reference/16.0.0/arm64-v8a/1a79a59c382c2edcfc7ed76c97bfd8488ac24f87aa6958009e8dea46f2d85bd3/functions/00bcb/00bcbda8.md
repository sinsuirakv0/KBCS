# 00bcbda8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcbda8",
  "name": "_ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae",
  "source_text_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae"
}
~~~

## 呼び出し元

- [00c5d5a0](../00c5d/00c5d5a0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 823 bytes

~~~c

void _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE(long param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  ulong uVar4;
  
  plVar2 = *(long **)(param_1 + 0x220);
  plVar3 = *(long **)(param_1 + 0x218);
  if (plVar2 != plVar3) {
    uVar4 = 0;
    plVar1 = (long *)*plVar3;
    plVar2 = plVar3;
    while( true ) {
      if (plVar1 != (long *)0x0) {
        (**(code **)(*plVar1 + 8))();
        plVar2 = *(long **)(param_1 + 0x218);
      }
      plVar2[uVar4] = 0;
      plVar2 = *(long **)(param_1 + 0x218);
      uVar4 = uVar4 + 1;
      if ((ulong)(*(long *)(param_1 + 0x220) - (long)plVar2 >> 3) <= uVar4) break;
                    /* catch() { ... } // from try @ 00bcbd90 with catch @ 00bcbdf4 */
      plVar1 = (long *)plVar2[uVar4];
    }
  }
  *(long **)(param_1 + 0x220) = plVar2;
  return;
}

~~~
