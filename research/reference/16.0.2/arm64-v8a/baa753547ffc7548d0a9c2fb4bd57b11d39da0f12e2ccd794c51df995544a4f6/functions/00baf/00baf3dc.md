# 00baf3dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baf340`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf340.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0038.md#compare-d58568f37efaaeca73766e8abdbbedc3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0035.md#compare-f67336d8f7e665523661e6d03f0eeea8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf3dc",
  "name": "_ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bee6be015250dbfdd050822998bedf2ad463ad1ef9811b6962e738382f57db35",
  "source_text_sha256": "bee6be015250dbfdd050822998bedf2ad463ad1ef9811b6962e738382f57db35"
}
~~~

## 呼び出し元

- [00c5d180](../00c5d/00c5d180.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1781 bytes

~~~c

int _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_
              (undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
              undefined8 *param_5)

{
  ulong uVar1;
  ulong uVar2;
  undefined8 uVar3;
  int iVar4;
  
  uVar1 = (*(code *)*param_5)(*param_2,*param_1);
  uVar2 = (*(code *)*param_5)(*param_3,*param_2);
  if ((uVar1 & 1) == 0) {
    if ((uVar2 & 1) == 0) {
      iVar4 = 0;
      goto LAB_00baf4c8;
    }
    uVar3 = *param_2;
    *param_2 = *param_3;
    *param_3 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_2,*param_1);
    if ((uVar1 & 1) == 0) goto LAB_00baf4bc;
    uVar3 = *param_1;
    *param_1 = *param_2;
    *param_2 = uVar3;
  }
  else {
    uVar3 = *param_1;
    if ((uVar2 & 1) != 0) {
      iVar4 = 1;
      *param_1 = *param_3;
      *param_3 = uVar3;
      goto LAB_00baf4c8;
    }
    *param_1 = *param_2;
    *param_2 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_3);
    if ((uVar1 & 1) == 0) {
LAB_00baf4bc:
      iVar4 = 1;
      goto LAB_00baf4c8;
    }
    uVar3 = *param_2;
    *param_2 = *param_3;
    *param_3 = uVar3;
  }
  iVar4 = 2;
LAB_00baf4c8:
  uVar1 = (*(code *)*param_5)(*param_4,*param_3);
  if ((uVar1 & 1) != 0) {
    uVar3 = *param_3;
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar1 = (*(code *)*param_5)(*param_3,*param_2);
    if ((uVar1 & 1) == 0) {
      iVar4 = iVar4 + 1;
    }
    else {
      uVar3 = *param_2;
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar1 = (*(code *)*param_5)(*param_2,*param_1);
      if ((uVar1 & 1) == 0) {
        iVar4 = iVar4 + 2;
      }
      else {
        uVar3 = *param_1;
        iVar4 = iVar4 + 3;
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  return iVar4;
}

~~~
