# 00ac8bec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00ac8bec",
  "name": "FUN_00ac8bec",
  "size": 1020,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bf4480b4598c92487e3d37d65ea235c74989e902f5c038f46cc13877f18625b",
  "source_text_sha256": "0bf4480b4598c92487e3d37d65ea235c74989e902f5c038f46cc13877f18625b"
}
~~~

## 呼び出し元

- [0078a084](../0078a/0078a084.md)
- [0083012c](../00830/0083012c.md)
- [008cc434](../008cc/008cc434.md)
- [008d41f8](../008d4/008d41f8.md)
- [008ffd30](../008ff/008ffd30.md)
- [00a3f25c](../00a3f/00a3f25c.md)
- [00a76e10](../00a76/00a76e10.md)
- [00ac1960](../00ac1/00ac1960.md)

## 呼び出し先

- [0045a0d4](../0045a/0045a0d4.md)
- [0046cd24](../0046c/0046cd24.md)
- [008524fc](../00852/008524fc.md)
- [00ac9044](../00ac9/00ac9044.md)

## 疑似コード / UTF-8 6342 bytes

~~~c

undefined8 FUN_00ac8bec(int *param_1)

{
  uint uVar1;
  char cVar2;
  undefined4 uVar3;
  long lVar4;
  long *plVar5;
  int iVar6;
  
  if (*param_1 != 0x7fffffff) {
    *param_1 = *param_1 + 1;
  }
  if ((char)param_1[0x28] != '\0') {
    iVar6 = param_1[0x29];
    param_1[0x29] = iVar6 + 1;
    if (iVar6 < 0x18) {
      return 1;
    }
    if (*(long **)(param_1 + 0x58) != (long *)0x0) {
      (**(code **)(**(long **)(param_1 + 0x58) + 0x30))();
      *(undefined1 *)(param_1 + 0x28) = 0;
      return 0;
    }
LAB_00ac8fe4:
                    /* WARNING: Subroutine does not return */
    FUN_0045a0d4();
  }
  lVar4 = FUN_008524fc();
  cVar2 = *(char *)((long)&fde_table_entry_00332a20.data_loc + lVar4);
  lVar4 = FUN_008524fc();
  if (cVar2 == '\0') {
    if (*(char *)((long)&fde_table_entry_00332a20.data_loc + lVar4 + 1) != '\0') {
      lVar4 = FUN_008524fc();
      cVar2 = *(char *)((long)param_1 + 0x1b9);
      *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) =
           *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) + 1;
      if (cVar2 != '\0') {
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4);
        lVar4 = FUN_008524fc();
        *(uint *)((long)&fde_table_entry_00334170.data_loc + lVar4) = iVar6 << 1 | 1;
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4);
        lVar4 = FUN_008524fc();
        *(uint *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = iVar6 << 1 | 1;
      }
      lVar4 = FUN_008524fc();
      if (0x128 < *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4)) {
        lVar4 = FUN_008524fc();
        *(undefined4 *)((long)&fde_table_entry_00334170.data_loc + lVar4) = 0x129;
        lVar4 = FUN_008524fc();
        *(undefined4 *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = 0x7e;
        lVar4 = FUN_008524fc();
        iVar6 = *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4);
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        lVar4 = FUN_008524fc();
        *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = iVar6 >> 1;
      }
      lVar4 = FUN_008524fc();
      uVar1 = *(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4);
      FUN_008524fc();
      FUN_008524fc();
      lVar4 = FUN_008524fc();
      if (uVar1 < 0xc) {
        lVar4 = FUN_008524fc();
        uVar3 = *(undefined4 *)
                 (PTR_DAT_00c9c5d0 +
                 (long)(int)~*(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) * 4 +
                 0x30);
        goto LAB_00ac8f6c;
      }
      *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0xb;
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = 0;
      lVar4 = FUN_008524fc();
      if ((*(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4) < 1) ||
         (*(char *)((long)param_1 + 0x1b9) == '\0')) {
        lVar4 = FUN_008524fc();
        *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar4 + 1) = 0;
        lVar4 = FUN_008524fc();
        plVar5 = *(long **)(param_1 + 0x40);
        *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0;
        if (plVar5 != (long *)0x0) {
          (**(code **)(*plVar5 + 0x30))();
          return 0;
        }
        goto LAB_00ac8fe4;
      }
    }
  }
  else {
    iVar6 = param_1[0x6e];
    *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) =
         *(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) + 1;
    if ((char)iVar6 != '\0') {
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4);
      lVar4 = FUN_008524fc();
      *(uint *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = iVar6 << 1 | 1;
    }
    lVar4 = FUN_008524fc();
    if (0x128 < *(int *)((long)&fde_table_entry_00334170.initial_loc + lVar4)) {
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00334170.initial_loc + lVar4) = 0x129;
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4);
      if (iVar6 < 0) {
        iVar6 = iVar6 + 1;
      }
      lVar4 = FUN_008524fc();
      *(int *)((long)&fde_table_entry_00334170.data_loc + lVar4) = iVar6 >> 1;
      lVar4 = FUN_008524fc();
      iVar6 = *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4);
      if (iVar6 < 0) {
        iVar6 = iVar6 + 1;
      }
      lVar4 = FUN_008524fc();
      *(int *)((long)&fde_table_entry_00333fa0.initial_loc + lVar4) = iVar6 >> 1;
    }
    lVar4 = FUN_008524fc();
    uVar1 = *(uint *)((long)&fde_table_entry_00333f90.initial_loc + lVar4);
    FUN_008524fc();
    FUN_008524fc();
    lVar4 = FUN_008524fc();
    if (uVar1 < 0xc) {
      uVar3 = *(undefined4 *)
               (PTR_DAT_00c9c5d0 +
               (long)*(int *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) * 4);
LAB_00ac8f6c:
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = uVar3;
    }
    else {
      *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0xb;
      FUN_008524fc();
      uVar3 = FUN_0046cd24();
      lVar4 = FUN_008524fc();
      *(undefined4 *)((long)&fde_table_entry_00333f80.data_loc + lVar4) = uVar3;
      lVar4 = FUN_008524fc();
      if ((*(int *)((long)&fde_table_entry_00334170.data_loc + lVar4) < 1) ||
         ((char)param_1[0x6e] == '\0')) {
        lVar4 = FUN_008524fc();
        *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar4) = 0;
        lVar4 = FUN_008524fc();
        plVar5 = *(long **)(param_1 + 0x4c);
        *(undefined4 *)((long)&fde_table_entry_00333f90.initial_loc + lVar4) = 0;
        if (plVar5 == (long *)0x0) goto LAB_00ac8fe4;
        (**(code **)(*plVar5 + 0x30))();
      }
    }
  }
  if (param_1[0x27] == 1) {
    iVar6 = param_1[0x26];
    param_1[0x26] = iVar6 + 1U;
    FUN_008524fc();
    if (iVar6 + 1U < 0x10) goto LAB_00ac8fc8;
    iVar6 = 0;
  }
  else {
    if ((param_1[0x27] != 2) || (iVar6 = param_1[0x26], param_1[0x26] = iVar6 + -1, 0 < iVar6))
    goto LAB_00ac8fc8;
    iVar6 = 3;
  }
  param_1[0x27] = iVar6;
LAB_00ac8fc8:
  FUN_00ac9044(param_1);
  return 1;
}

~~~
