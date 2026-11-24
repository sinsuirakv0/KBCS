# 004cbadc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004cba9c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0009.md#compare-49a146afe99110ce662ab7132081894c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0009.md#compare-80ae920471be812b1b1cb62ca49795e4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cbadc",
  "name": "FUN_004cbadc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac60836151a9c6309bad750ccce6a04e3d895912e15085e6d631feba598b93d2",
  "source_text_sha256": "ac60836151a9c6309bad750ccce6a04e3d895912e15085e6d631feba598b93d2"
}
~~~

## 呼び出し元

- [004c130c](../004c1/004c130c.md)
- [00530dfc](../00530/00530dfc.md)

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58b00](../00c58/00c58b00.md)
- [00c58b10](../00c58/00c58b10.md)

## 疑似コード / UTF-8 2077 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_004cbadc(long *param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined *puVar4;
  void *pvVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  long lVar8;
  
  lVar1 = tpidr_el0;
  lVar8 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan16MDx_HashFunctionE_00c9b008 + 0x10);
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[1] = 0;
  pvVar5 = calloc(0x40,1);
  if (pvVar5 == (void *)0x0) {
    uVar7 = __cxa_allocate_exception(8);
    if (*(long *)(lVar1 + 0x28) == lVar8) {
      _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9aeb8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9aec0);
    }
  }
  else {
    param_1[2] = (long)pvVar5 + 0x40;
    param_1[3] = (long)pvVar5 + 0x40;
    *(undefined2 *)(param_1 + 6) = 0x101;
    param_1[4] = 0;
    param_1[7] = 8;
    puVar4 = PTR__ZTVN5Botan7SHA_256E_00c9b020;
    param_1[5] = 0;
    param_1[9] = 0;
    param_1[10] = 0;
    *param_1 = (long)(puVar4 + 0x10);
    param_1[1] = (long)pvVar5;
    param_1[8] = 0;
    puVar6 = calloc(8,4);
    if (puVar6 == (undefined8 *)0x0) {
      uVar7 = __cxa_allocate_exception(8);
      if (*(long *)(lVar1 + 0x28) == lVar8) {
        _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
        __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9aeb8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9aec0
                   );
      }
    }
    else {
      param_1[4] = 0;
      param_1[5] = 0;
      param_1[8] = (long)puVar6;
      param_1[9] = (long)(puVar6 + 4);
      param_1[10] = (long)(puVar6 + 4);
      uVar3 = _DAT_002c31a0;
      uVar2 = _UNK_002c2d38;
      uVar7 = _DAT_002c2d30;
      puVar6[1] = _UNK_002c31a8;
      *puVar6 = uVar3;
      puVar6[3] = uVar2;
      puVar6[2] = uVar7;
      if (*(long *)(lVar1 + 0x28) == lVar8) {
        return;
      }
    }
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
