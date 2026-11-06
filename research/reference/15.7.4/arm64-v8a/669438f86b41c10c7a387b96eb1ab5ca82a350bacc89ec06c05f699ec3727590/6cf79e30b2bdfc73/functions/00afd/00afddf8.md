# 00afddf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00afddf8.md)

## 関数情報

~~~json
{
  "address": "00afddf8",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edc168672f43c5a0b06824bbe30d7e0b8bb0a164ed8439db4db17ff11d9130a3",
  "source_text_sha256": "edc168672f43c5a0b06824bbe30d7e0b8bb0a164ed8439db4db17ff11d9130a3"
}
~~~
## 呼び出し元

- [00bded20](../00bde/00bded20.md)

## 呼び出し先

- [00afd2ac](../00afd/00afd2ac.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb200](../00bdb/00bdb200.md)
- [00bde230](../00bde/00bde230.md)
- [00bded40](../00bde/00bded40.md)

## 疑似コード 1/1 / UTF-8 4076 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_
               (undefined8 *param_1,undefined8 param_2,undefined8 param_3)

{
  byte *pbVar1;
  byte *pbVar2;
  size_t __n;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  long lVar6;
  void *pvVar7;
  byte *pbVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  byte *pbVar11;
  byte *pbVar12;
  int iVar13;
  ulong uVar14;
  byte *__s1;
  byte *__s2;
  byte local_b8 [8];
  ulong local_b0;
  void *local_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  byte *local_88;
  byte *local_80;
  byte *local_70;
  byte *local_68;
  long local_58;
  
  lVar6 = tpidr_el0;
  local_58 = *(long *)(lVar6 + 0x28);
  _ZNK8firebase4Path14GetDirectoriesEv(&local_70);
  _ZNK8firebase4Path14GetDirectoriesEv(&local_88,param_3);
  pbVar12 = local_68;
  pbVar11 = local_80;
  pbVar8 = local_88;
  pbVar2 = local_88;
  pbVar1 = local_70;
  do {
    if (pbVar1 == pbVar12) {
      FUN_00afd2ac(local_b8,pbVar2,pbVar11);
      uVar14 = (ulong)(local_b8[0] >> 1);
      pvVar7 = (void *)((ulong)local_b8 | 1);
      if ((local_b8[0] & 1) != 0) {
        uVar14 = local_b0;
        pvVar7 = local_a8;
      }
      uStack_98 = 0;
      local_90 = 0;
      local_a0 = 0;
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_a0,pvVar7,uVar14);
      uVar10 = uStack_98;
      uVar9 = local_a0;
      local_a0 = 0;
      uStack_98 = 0;
      *(undefined1 *)(param_1 + 3) = 1;
      param_1[2] = local_90;
      param_1[1] = uVar10;
      *param_1 = uVar9;
      local_90 = 0;
      pbVar8 = local_88;
      pbVar1 = local_88;
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
        pbVar8 = local_88;
        pbVar1 = local_88;
      }
joined_r0x00afdf80:
      if (pbVar8 != (byte *)0x0) {
        local_88 = pbVar8;
        if (local_80 != pbVar8) {
          bVar4 = local_80[-0x18];
          pbVar2 = local_80 + -0x18;
          local_88 = pbVar1;
          while( true ) {
            pbVar1 = pbVar2;
            if ((bVar4 & 1) != 0) {
              _ZdlPv(*(void **)(local_80 + -8));
            }
            if (pbVar8 == pbVar1) break;
            bVar4 = pbVar1[-0x18];
            pbVar2 = pbVar1 + -0x18;
            local_80 = pbVar1;
          }
        }
        _ZdlPv(local_88);
      }
      pbVar1 = local_70;
      if (local_70 != (byte *)0x0) {
        if (local_68 != local_70) {
          bVar4 = local_68[-0x18];
          pbVar2 = local_68 + -0x18;
          while( true ) {
            pbVar8 = pbVar2;
            if ((bVar4 & 1) != 0) {
              _ZdlPv(*(void **)(local_68 + -8));
            }
            if (pbVar1 == pbVar8) break;
            bVar4 = pbVar8[-0x18];
            pbVar2 = pbVar8 + -0x18;
            local_68 = pbVar8;
          }
        }
        local_68 = pbVar1;
        _ZdlPv(local_70);
      }
      if (*(long *)(lVar6 + 0x28) == local_58) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (pbVar11 == pbVar2) {
LAB_00afdefc:
      *(undefined1 *)(param_1 + 3) = 0;
      pbVar1 = local_88;
      goto joined_r0x00afdf80;
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
    if (__n != sVar3) goto LAB_00afdefc;
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
          if (pbVar1[uVar14 + 1] != __s2[uVar14]) goto LAB_00afdefc;
          uVar14 = uVar14 + 1;
        } while (bVar4 >> 1 != uVar14);
      }
    }
    else if ((__n != 0) && (iVar13 = memcmp(__s1,__s2,__n), iVar13 != 0)) goto LAB_00afdefc;
    pbVar1 = pbVar1 + 0x18;
    pbVar2 = pbVar2 + 0x18;
  } while( true );
}

~~~
