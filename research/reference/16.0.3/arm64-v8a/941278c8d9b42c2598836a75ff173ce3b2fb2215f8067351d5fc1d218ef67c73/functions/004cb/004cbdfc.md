# 004cbdfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004cbdfc",
  "name": "FUN_004cbdfc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8d52722b0ef2ca74c4ea4a2e20c54653235568a1de1ee9d776d556c632056a7",
  "source_text_sha256": "c8d52722b0ef2ca74c4ea4a2e20c54653235568a1de1ee9d776d556c632056a7"
}
~~~

## 呼び出し元

- [004c162c](../004c1/004c162c.md)
- [0053111c](../00531/0053111c.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59ad0](../00c59/00c59ad0.md)
- [00c59ae0](../00c59/00c59ae0.md)

## 疑似コード / UTF-8 2077 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_004cbdfc(long *param_1)

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
  *param_1 = (long)(PTR__ZTVN5Botan16MDx_HashFunctionE_00c9bfd8 + 0x10);
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[1] = 0;
  pvVar5 = calloc(0x40,1);
  if (pvVar5 == (void *)0x0) {
    uVar7 = __cxa_allocate_exception(8);
    if (*(long *)(lVar1 + 0x28) == lVar8) {
      _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9be88,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9be90);
    }
  }
  else {
    param_1[2] = (long)pvVar5 + 0x40;
    param_1[3] = (long)pvVar5 + 0x40;
    *(undefined2 *)(param_1 + 6) = 0x101;
    param_1[4] = 0;
    param_1[7] = 8;
    puVar4 = PTR__ZTVN5Botan7SHA_256E_00c9bff0;
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
        __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9be88,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9be90
                   );
      }
    }
    else {
      param_1[4] = 0;
      param_1[5] = 0;
      param_1[8] = (long)puVar6;
      param_1[9] = (long)(puVar6 + 4);
      param_1[10] = (long)(puVar6 + 4);
      uVar3 = _DAT_002c31f0;
      uVar2 = _UNK_002c2d88;
      uVar7 = _DAT_002c2d80;
      puVar6[1] = _UNK_002c31f8;
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
