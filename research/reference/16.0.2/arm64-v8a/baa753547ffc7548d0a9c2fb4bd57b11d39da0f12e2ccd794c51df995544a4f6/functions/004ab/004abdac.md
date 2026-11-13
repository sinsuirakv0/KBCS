# 004abdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "004abdac",
  "name": "_ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_",
  "size": 644,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42ca49d4938130bfc35f60a504b42dbaa1eacb79c5331477c17cd9dea0b10047",
  "source_text_sha256": "42ca49d4938130bfc35f60a504b42dbaa1eacb79c5331477c17cd9dea0b10047"
}
~~~

## 呼び出し元

- [00c58990](../00c58/00c58990.md)

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c58730](../00c58/00c58730.md)
- [00c587f0](../00c58/00c587f0.md)
- [00c58800](../00c58/00c58800.md)
- [00c589f0](../00c58/00c589f0.md)
- [00c58a00](../00c58/00c58a00.md)
- [0112a058](../0112a/0112a058.md)

## 疑似コード / UTF-8 3541 bytes

~~~c

undefined8
_ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_
          (undefined8 param_1,void **param_2,undefined4 param_3,undefined4 param_4)

{
  int *piVar1;
  undefined4 uVar2;
  char cVar3;
  char cVar4;
  long lVar5;
  uint uVar6;
  char *pcVar7;
  void *pvVar8;
  long lVar9;
  void *pvVar10;
  undefined1 auStack_98 [8];
  char *local_90;
  char *local_88;
  long local_80;
  void *local_78;
  void *local_70;
  void *pvStack_68;
  undefined4 local_60;
  long local_58;
  
  lVar5 = tpidr_el0;
  local_58 = *(long *)(lVar5 + 0x28);
  _ZN5Botan11BER_Decoder15get_next_objectEv(auStack_98);
  _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_(auStack_98,param_3,param_4);
  if (local_90 == local_88) {
    _ZN5Botan6BigIntC1Em(&local_78,0);
    if (&local_78 != param_2) {
      pvVar10 = param_2[2];
      pvVar8 = *param_2;
      *param_2 = local_78;
      uVar2 = *(undefined4 *)(param_2 + 3);
      param_2[2] = pvStack_68;
      param_2[1] = local_70;
      *(undefined4 *)(param_2 + 3) = local_60;
      local_78 = pvVar8;
      pvStack_68 = pvVar10;
      local_60 = uVar2;
    }
    pvVar8 = local_78;
    pcVar7 = local_90;
    if (local_78 != (void *)0x0) {
      local_70 = local_78;
      (*(code *)PTR_memset_00c67808)(local_78,0,(long)pvStack_68 - (long)local_78);
      free(pvVar8);
      pcVar7 = local_90;
    }
  }
  else {
    cVar4 = *local_90;
    pcVar7 = local_88;
    if (cVar4 < '\0') {
      pcVar7 = local_88 + ~(ulong)local_90;
      do {
        if (pcVar7 == (char *)0xffffffffffffffff) break;
        cVar3 = local_90[(long)pcVar7];
        local_90[(long)pcVar7] = cVar3 + -1;
        pcVar7 = pcVar7 + -1;
      } while (cVar3 == '\0');
      pcVar7 = local_90;
      if (local_88 != local_90) {
        lVar9 = 0;
        do {
          local_90[lVar9] = ~local_90[lVar9];
          lVar9 = lVar9 + 1;
          pcVar7 = local_88;
        } while (lVar9 != (long)local_88 - (long)local_90);
      }
    }
    _ZN5Botan6BigIntC1EPKhmNS0_4BaseE(&local_78,local_90,(long)pcVar7 - (long)local_90,0x100);
    if (&local_78 != param_2) {
      pvVar10 = param_2[2];
      pvVar8 = *param_2;
      *param_2 = local_78;
      uVar2 = *(undefined4 *)(param_2 + 3);
      param_2[2] = pvStack_68;
      param_2[1] = local_70;
      *(undefined4 *)(param_2 + 3) = local_60;
      local_78 = pvVar8;
      pvStack_68 = pvVar10;
      local_60 = uVar2;
    }
    pvVar8 = local_78;
    if (local_78 != (void *)0x0) {
      local_70 = local_78;
      (*(code *)PTR_memset_00c67808)(local_78,0,(long)pvStack_68 - (long)local_78);
      free(pvVar8);
    }
    pcVar7 = local_90;
    if (cVar4 < '\0') {
      piVar1 = *param_2;
      uVar6 = (uint)(*(int *)(param_2 + 3) != 1);
      lVar9 = (long)param_2[1] - (long)piVar1 >> 2;
      if ((long)param_2[1] - (long)piVar1 == 0) {
joined_r0x004ac004:
        do {
          if (lVar9 == 0) goto LAB_004ac018;
          if (*piVar1 != 0) goto LAB_004ac01c;
          lVar9 = lVar9 + -1;
          piVar1 = piVar1 + 1;
        } while( true );
      }
      do {
        if (piVar1[lVar9 + -1] != 0) goto joined_r0x004ac004;
        lVar9 = lVar9 + -1;
      } while (lVar9 != 0);
LAB_004ac018:
      uVar6 = 1;
LAB_004ac01c:
      *(uint *)(param_2 + 3) = uVar6;
    }
  }
  if (pcVar7 != (char *)0x0) {
    (*(code *)PTR_memset_00c67808)(pcVar7,0,local_80 - (long)pcVar7);
    free(pcVar7);
  }
  if (*(long *)(lVar5 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return param_1;
}

~~~
