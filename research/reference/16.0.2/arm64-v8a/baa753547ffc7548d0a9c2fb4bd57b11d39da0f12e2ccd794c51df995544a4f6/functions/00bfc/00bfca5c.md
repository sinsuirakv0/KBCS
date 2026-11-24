# 00bfca5c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc9c0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-35b16e94d3d1f909cea4456b2fe402f4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0099.md#compare-a7658b4cb10fb840f4cc222aae451b2c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfca5c",
  "name": "FUN_00bfca5c",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd26bf10f0cfc0cc890e92bc0cd8866892b8f82f4682c034886d6b567a052ab9",
  "source_text_sha256": "cd26bf10f0cfc0cc890e92bc0cd8866892b8f82f4682c034886d6b567a052ab9"
}
~~~

## 呼び出し元

- [00bfca54](../00bfc/00bfca54.md)

## 呼び出し先

- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

## 疑似コード / UTF-8 1296 bytes

~~~c

long * FUN_00bfca5c(long *param_1,undefined4 *param_2)

{
  long lVar1;
  long *plVar2;
  undefined4 uVar3;
  undefined1 auStack_38 [8];
  long local_30;
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] == '\0') {
    return param_1;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,
                              PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9bbe0
                             );
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  (**(code **)(*plVar2 + 0x20))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,&local_30);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  if (local_30 < -0x80000000) {
    uVar3 = 0x80000000;
  }
  else {
    if (local_30 < 0x80000000) {
      *param_2 = (int)local_30;
      goto LAB_00bfcb2c;
    }
    uVar3 = 0x7fffffff;
  }
  local_24 = local_24 | 4;
  *param_2 = uVar3;
LAB_00bfcb2c:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  return param_1;
}

~~~
