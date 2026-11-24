# 00bb1eac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb1e10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1e10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0010.md#compare-28d379302bc0723dd82f05d881987e5f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0036.md#compare-28efa0be6dc68d9a6652ab0cda67bfc9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb1eac",
  "name": "FUN_00bb1eac",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d0d14b30347854c45f70a7c52cdd32f7a6ecbd598f596afd37e15b3fd05348c",
  "source_text_sha256": "5d0d14b30347854c45f70a7c52cdd32f7a6ecbd598f596afd37e15b3fd05348c"
}
~~~

## 呼び出し元

- [00bb1810](../00bb1/00bb1810.md)
- [00bb2110](../00bb2/00bb2110.md)

## 呼び出し先

- [00c5d170](../00c5d/00c5d170.md)

## 疑似コード / UTF-8 1247 bytes

~~~c

int FUN_00bb1eac(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                undefined8 *param_5,undefined8 *param_6)

{
  int iVar1;
  ulong uVar2;
  undefined8 uVar3;
  
  iVar1 = _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_();
  uVar2 = (*(code *)*param_6)(*param_5,*param_4);
  if ((uVar2 & 1) != 0) {
    uVar3 = *param_4;
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar2 = (*(code *)*param_6)(*param_4,*param_3);
    if ((uVar2 & 1) == 0) {
      iVar1 = iVar1 + 1;
    }
    else {
                    /* catch() { ... } // from try @ 00bb2100 with catch @ 00bb1f24 */
      uVar3 = *param_3;
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar2 = (*(code *)*param_6)(*param_3,*param_2);
      if ((uVar2 & 1) == 0) {
        iVar1 = iVar1 + 2;
      }
      else {
        uVar3 = *param_2;
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar2 = (*(code *)*param_6)(*param_2,*param_1);
        if ((uVar2 & 1) == 0) {
          iVar1 = iVar1 + 3;
        }
        else {
          uVar3 = *param_1;
          iVar1 = iVar1 + 4;
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return iVar1;
}

~~~
