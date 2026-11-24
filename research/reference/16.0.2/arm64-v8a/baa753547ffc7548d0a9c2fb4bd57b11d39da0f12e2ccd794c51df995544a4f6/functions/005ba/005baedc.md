# 005baedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005bae9c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bae9c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0016.md#compare-fedd9cbf9366b247b5c1a9cdb754d8cf)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0024.md#compare-0010af965fdec3d600df44fb5a5d3675)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005baedc",
  "name": "FUN_005baedc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a3fc2c1a016cfee1d2d0a5f9fd7557626e5ac8b68751bbb689ec41b4e59a243",
  "source_text_sha256": "2a3fc2c1a016cfee1d2d0a5f9fd7557626e5ac8b68751bbb689ec41b4e59a243"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58200](../00c58/00c58200.md)
- [00c58210](../00c58/00c58210.md)
- [00c58220](../00c58/00c58220.md)

## 疑似コード / UTF-8 1344 bytes

~~~c

undefined8 FUN_005baedc(undefined8 *param_1)

{
  pthread_key_t __key;
  long lVar1;
  pthread_key_t *ppVar2;
  void *pvVar3;
  long lVar4;
  code *pcVar5;
  
  lVar1 = tpidr_el0;
  lVar4 = *(long *)(lVar1 + 0x28);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bae78 with catch @ 005baf04
                        */
  ppVar2 = (pthread_key_t *)_ZNSt6__ndk119__thread_local_dataEv();
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bae14 with catch @ 005baf08
                        */
  pvVar3 = (void *)*param_1;
  __key = *ppVar2;
  *param_1 = 0;
  pthread_setspecific(__key,pvVar3);
  pcVar5 = (code *)param_1[1];
  if ((param_1[2] & 1) != 0) {
    pcVar5 = *(code **)(pcVar5 + *(long *)(param_1[3] + ((long)param_1[2] >> 1)));
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bafdc with catch @ 005baf30
                        */
  (*pcVar5)();
  pvVar3 = (void *)*param_1;
  *param_1 = 0;
  if (pvVar3 != (void *)0x0) {
    _ZNSt6__ndk115__thread_structD1Ev(pvVar3);
    _ZdlPv(pvVar3);
  }
  if (*(long *)(lVar1 + 0x28) == lVar4) {
                    /* try { // try from 005baf64 to 006baf7b has its CatchHandler @ 005bb00c */
    _ZdlPv(param_1);
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
