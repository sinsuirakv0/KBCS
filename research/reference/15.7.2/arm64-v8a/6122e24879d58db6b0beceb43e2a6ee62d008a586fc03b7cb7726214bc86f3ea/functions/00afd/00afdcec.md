# 00afdcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afdcec.md)

## 関数情報

~~~json
{
  "address": "00afdcec",
  "name": "firebase::Path::GetRelative",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58782ab0d32d02bdf786ea9808f67b1704ef9f6774c8b6201930cd66683493c4",
  "source_text_sha256": "58782ab0d32d02bdf786ea9808f67b1704ef9f6774c8b6201930cd66683493c4"
}
~~~
## 呼び出し元

- [00bdec20](../00bde/00bdec20.md)

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb100](../00bdb/00bdb100.md)
- [00bde130](../00bde/00bde130.md)
- [00bdec40](../00bde/00bdec40.md)

## 疑似コード 1/1 / UTF-8 4647 bytes

~~~c

/* firebase::Path::GetRelative(firebase::Path const&, firebase::Path const&) */

void firebase::Path::GetRelative(Path *param_1,Path *param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  size_t __n;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  long lVar6;
  char *pcVar7;
  byte *pbVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  byte *pbVar11;
  byte *pbVar12;
  int iVar13;
  undefined8 *in_x8;
  ulong uVar14;
  byte *__s1;
  byte *__s2;
  byte local_b8 [8];
  ulong local_b0;
  char *local_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  byte *local_88;
  byte *local_80;
  byte *local_70;
  byte *local_68;
  long local_58;
  
                    /* try { // try from 00afdcfc to 00bfdd07 has its CatchHandler @ 00afebe4 */
                    /* try { // try from 00afdd08 to 00bfdd1f has its CatchHandler @ 00afeb88 */
  lVar6 = tpidr_el0;
  local_58 = *(long *)(lVar6 + 0x28);
                    /* try { // try from 00afdd20 to 00c00b67 has its CatchHandler @ 00af560c */
  GetDirectories();
  GetDirectories();
  pbVar12 = local_68;
  pbVar11 = local_80;
  pbVar8 = local_88;
  pbVar2 = local_88;
  pbVar1 = local_70;
  do {
    if (pbVar1 == pbVar12) {
      FUN_00afd1a0(local_b8,pbVar2,pbVar11);
      uVar14 = (ulong)(local_b8[0] >> 1);
      pcVar7 = (char *)((ulong)local_b8 | 1);
      if ((local_b8[0] & 1) != 0) {
        uVar14 = local_b0;
        pcVar7 = local_a8;
      }
      uStack_98 = 0;
      local_90 = 0;
      local_a0 = 0;
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &local_a0,pcVar7,uVar14);
      uVar10 = uStack_98;
      uVar9 = local_a0;
      local_a0 = 0;
      uStack_98 = 0;
      *(undefined1 *)(in_x8 + 3) = 1;
      in_x8[2] = local_90;
      in_x8[1] = uVar10;
      *in_x8 = uVar9;
      local_90 = 0;
      pbVar8 = local_88;
      pbVar1 = local_88;
      if ((local_b8[0] & 1) != 0) {
        operator_delete(local_a8);
        pbVar8 = local_88;
        pbVar1 = local_88;
      }
joined_r0x00afde74:
      if (pbVar8 != (byte *)0x0) {
        local_88 = pbVar8;
        if (local_80 != pbVar8) {
          bVar4 = local_80[-0x18];
          pbVar2 = local_80 + -0x18;
          local_88 = pbVar1;
          while( true ) {
            pbVar1 = pbVar2;
            if ((bVar4 & 1) != 0) {
              operator_delete(*(void **)(local_80 + -8));
            }
            if (pbVar8 == pbVar1) break;
            bVar4 = pbVar1[-0x18];
            pbVar2 = pbVar1 + -0x18;
            local_80 = pbVar1;
          }
        }
        operator_delete(local_88);
      }
      pbVar1 = local_70;
      if (local_70 != (byte *)0x0) {
        if (local_68 != local_70) {
          bVar4 = local_68[-0x18];
          pbVar2 = local_68 + -0x18;
          while( true ) {
            pbVar8 = pbVar2;
            if ((bVar4 & 1) != 0) {
              operator_delete(*(void **)(local_68 + -8));
            }
            if (pbVar1 == pbVar8) break;
            bVar4 = pbVar8[-0x18];
            pbVar2 = pbVar8 + -0x18;
            local_68 = pbVar8;
          }
        }
        local_68 = pbVar1;
        operator_delete(local_70);
      }
      if (*(long *)(lVar6 + 0x28) == local_58) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (pbVar11 == pbVar2) {
LAB_00afddf0:
      *(undefined1 *)(in_x8 + 3) = 0;
      pbVar1 = local_88;
      goto joined_r0x00afde74;
    }
    bVar4 = *pbVar1;
    bVar5 = *pbVar2;
    __n = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      __n = *(size_t *)(pbVar1 + 8);
    }
    sVar3 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      sVar3 = *(size_t *)(pbVar2 + 8);
    }
    if (__n != sVar3) goto LAB_00afddf0;
    __s1 = *(byte **)(pbVar1 + 0x10);
    __s2 = *(byte **)(pbVar2 + 0x10);
    if ((bVar4 & 1) == 0) {
      __s1 = pbVar1 + 1;
    }
    if ((bVar5 & 1) == 0) {
      __s2 = pbVar2 + 1;
    }
    if ((bVar4 & 1) == 0) {
      if (__n != 0) {
        uVar14 = 0;
        do {
          if (pbVar1[uVar14 + 1] != __s2[uVar14]) goto LAB_00afddf0;
          uVar14 = uVar14 + 1;
        } while (bVar4 >> 1 != uVar14);
      }
    }
    else if ((__n != 0) && (iVar13 = memcmp(__s1,__s2,__n), iVar13 != 0)) goto LAB_00afddf0;
    pbVar1 = pbVar1 + 0x18;
    pbVar2 = pbVar2 + 0x18;
  } while( true );
}

~~~
