# 00bbfa8c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbf9c4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-ba49a37d450841a91cb8c18c3a1c16bf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbfad0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-75a549b12567d9200c67c88218008af4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfa8c",
  "name": "FUN_00bbfa8c",
  "size": 808,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98921324be1e0f1ab1c8ead401043e8d282d03dd332bc83d74e5e82d24a23a74",
  "source_text_sha256": "98921324be1e0f1ab1c8ead401043e8d282d03dd332bc83d74e5e82d24a23a74",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfa8c",
        "00bbfdb3"
      ]
    ],
    "bytes_sha256": "c2663312c4f3345857683d2d4bb4d4c77bf4198e4ae6fe4ad0ca49f9435705d1",
    "instruction_count": 202,
    "instruction_bytes": 808,
    "body_bytes": 808,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbfa8c](../00bbf/00bbfa8c.md)
- [00bc1710](../00bc1/00bc1710.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)

## 呼び出し先

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbde18](../00bbd/00bbde18.md)
- [00bbfa8c](../00bbf/00bbfa8c.md)
- [00bbff2c](../00bbf/00bbff2c.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)
- [00bc489c](../00bc4/00bc489c.md)
- [00bca980](../00bca/00bca980.md)
- [00bdb130](../00bdb/00bdb130.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 関連文字列（未確認候補）

~~~text
"yptnk"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5841 bytes

~~~c

undefined8 * FUN_00bbfa8c(long *param_1)

{
  long *__src;
  undefined8 *puVar1;
  long lVar2;
  long *__ptr;
  void *pvVar3;
  char *pcVar4;
  long lVar5;
  byte *pbVar6;
  long lVar7;
  undefined **ppuVar8;
  undefined1 uVar9;
  byte *pbVar10;
  uint uVar11;
  size_t __n;
  long *plVar12;
  undefined1 auVar13 [16];
  
  pbVar6 = (byte *)*param_1;
  pbVar10 = (byte *)param_1[1];
  if (pbVar10 == pbVar6) {
    uVar11 = 0;
  }
  else {
    uVar11 = (uint)*pbVar6;
  }
  uVar11 = uVar11 - 0x4a >> 1 | uVar11 << 0x1f;
                    /* try { // try from 00bbfac8 to 00cbfacb has its CatchHandler @ 00bc8ae8 */
  if ((int)uVar11 < 5) {
    if (uVar11 == 0) {
      lVar7 = param_1[2];
      lVar5 = param_1[3];
      pbVar6 = pbVar6 + 1;
      __src = param_1 + 5;
      *param_1 = (long)pbVar6;
      while ((pbVar6 == pbVar10 || (*pbVar6 != 0x45))) {
        lVar2 = FUN_00bbfa8c(param_1);
        if (lVar2 == 0) {
          return (undefined8 *)0x0;
        }
        plVar12 = (long *)param_1[3];
        if (plVar12 == (long *)param_1[4]) {
          __ptr = (long *)param_1[2];
          __n = (long)plVar12 - (long)__ptr;
          if (__ptr == __src) {
            pvVar3 = malloc(__n * 2);
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
            if (plVar12 != __src) {
              memcpy(pvVar3,__src,__n);
            }
                    /* try { // try from 00bbfc08 to 00cbfc1b has its CatchHandler @ 00bc87a8 */
            param_1[2] = (long)pvVar3;
          }
          else {
            pvVar3 = realloc(__ptr,__n * 2);
            param_1[2] = (long)pvVar3;
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
          }
          plVar12 = (long *)((long)pvVar3 + __n);
          param_1[4] = (long)((long)pvVar3 + ((long)__n >> 2) * 8);
        }
        param_1[3] = (long)(plVar12 + 1);
                    /* try { // try from 00bbfb94 to 00cbfb97 has its CatchHandler @ 00bc884c */
        *plVar12 = lVar2;
        pbVar10 = (byte *)param_1[1];
                    /* try { // try from 00bbfb98 to 00cbfc07 has its CatchHandler @ 00bbf52c */
        pbVar6 = (byte *)*param_1;
      }
      *param_1 = (long)(pbVar6 + 1);
      auVar13 = FUN_00bbff2c(param_1,lVar5 - lVar7 >> 3);
      pvVar3 = (void *)param_1[0x266];
                    /* try { // try from 00bbfc70 to 00cbfc7b has its CatchHandler @ 00bc8a2c */
      lVar7 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfc7c to 00cbfc8b has its CatchHandler @ 00bc8a24 */
      puVar1 = pvVar3;
      if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
        puVar1 = malloc(0x1000);
        if (puVar1 == (void *)0x0) {
LAB_00bbfdb0:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar7 = 0;
        *puVar1 = pvVar3;
        puVar1[1] = 0;
        param_1[0x266] = (long)puVar1;
      }
      lVar5 = (long)puVar1 + lVar7;
                    /* try { // try from 00bbfcac to 00cbfd1f has its CatchHandler @ 00bc8b80 */
      ppuVar8 = &PTR_FUN_00c197b8;
      *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
      uVar9 = 0x29;
LAB_00bbfcbc:
      *(undefined8 *)(lVar5 + 0x10) = ppuVar8;
      *(undefined1 *)(lVar5 + 0x18) = uVar9;
      *(undefined1 (*) [16])(lVar5 + 0x20) = auVar13;
      *(ushort *)(lVar5 + 0x19) = *(ushort *)(lVar5 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar5 + 0x10);
    }
    if (uVar11 == 1) {
      if (((ulong)((long)pbVar10 - (long)pbVar6) < 2) || (pbVar6[1] != 0x5a)) {
        puVar1 = (undefined8 *)FUN_00bc489c(param_1);
        return puVar1;
      }
      *param_1 = (long)(pbVar6 + 2);
      puVar1 = (undefined8 *)FUN_00bbd2c4(param_1);
joined_r0x00bbfb28:
      if (puVar1 != (undefined8 *)0x0) {
        pcVar4 = (char *)*param_1;
                    /* try { // try from 00bbfb30 to 00cbfb33 has its CatchHandler @ 00bc8a8c */
        if ((pcVar4 == (char *)param_1[1]) || (*pcVar4 != 'E')) {
          puVar1 = (undefined8 *)0x0;
        }
        else {
          *param_1 = (long)(pcVar4 + 1);
        }
      }
      return puVar1;
    }
  }
  else if (uVar11 == 5) {
    if ((pbVar10 != pbVar6) && (*pbVar6 == 0x54)) {
      if ((ulong)((long)pbVar10 - (long)pbVar6) < 2) {
        uVar11 = 0;
      }
      else {
        uVar11 = (uint)pbVar6[1];
      }
      pcVar4 = memchr("yptnk",uVar11,5);
      if ((pcVar4 != (char *)0x0) && (pcVar4 != "")) {
        lVar7 = FUN_00bca980(param_1,0);
        if (lVar7 == 0) {
          return (undefined8 *)0x0;
        }
        lVar5 = FUN_00bbfa8c(param_1);
        auVar13._8_8_ = lVar5;
        auVar13._0_8_ = lVar7;
                    /* try { // try from 00bbfd38 to 00cbfd3f has its CatchHandler @ 00bc8ae8 */
        if (lVar5 == 0) {
          return (undefined8 *)0x0;
        }
        pvVar3 = (void *)param_1[0x266];
        lVar7 = *(long *)((long)pvVar3 + 8);
        puVar1 = pvVar3;
        if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
          puVar1 = malloc(0x1000);
          if (puVar1 == (void *)0x0) goto LAB_00bbfdb0;
          lVar7 = 0;
          *puVar1 = pvVar3;
          puVar1[1] = 0;
                    /* try { // try from 00bbfd68 to 00cbfd7b has its CatchHandler @ 00bc87a4 */
          param_1[0x266] = (long)puVar1;
        }
        lVar5 = (long)puVar1 + lVar7;
        ppuVar8 = &PTR_FUN_00c19828;
        *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
        uVar9 = 0x22;
        goto LAB_00bbfcbc;
      }
    }
  }
  else if (uVar11 == 7) {
    *param_1 = (long)(pbVar6 + 1);
    puVar1 = (undefined8 *)FUN_00bc2ec8(param_1);
    goto joined_r0x00bbfb28;
  }
  puVar1 = (undefined8 *)FUN_00bbde18(param_1);
  return puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfa8c"></a> `00bbfa8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfa90"></a> `00bbfa90` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbfa94"></a> `00bbfa94` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfa98"></a> `00bbfa98` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfa9c"></a> `00bbfa9c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfaa0"></a> `00bbfaa0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfaa4"></a> `00bbfaa4` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bbfaa8"></a> `00bbfaa8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbfaac"></a> `00bbfaac` | `2a 01 08 eb` | subs x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfab0"></a> `00bbfab0` | `60 00 00 54` | b.eq 0x00bbfabc | `CONDITIONAL_JUMP`
<a id="insn-00bbfab4"></a> `00bbfab4` | `0b 01 40 39` | ldrb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bbfab8"></a> `00bbfab8` | `02 00 00 14` | b 0x00bbfac0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfabc"></a> `00bbfabc` | `eb 03 1f 2a` | mov w11,wzr | `FALL_THROUGH`
<a id="insn-00bbfac0"></a> `00bbfac0` | `6b 29 01 51` | sub w11,w11,#0x4a | `FALL_THROUGH`
<a id="insn-00bbfac4"></a> `00bbfac4` | `6b 05 8b 13` | ror w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfac8"></a> `00bbfac8` | `7f 11 00 71` | cmp w11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfacc"></a> `00bbfacc` | `ec 01 00 54` | b.gt 0x00bbfb08 | `CONDITIONAL_JUMP`
<a id="insn-00bbfad0"></a> `00bbfad0` | `0b 04 00 34` | cbz w11,0x00bbfb50 | `CONDITIONAL_JUMP`
<a id="insn-00bbfad4"></a> `00bbfad4` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfad8"></a> `00bbfad8` | `a1 15 00 54` | b.ne 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfadc"></a> `00bbfadc` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfae0"></a> `00bbfae0` | `a3 0a 00 54` | b.cc 0x00bbfc34 | `CONDITIONAL_JUMP`
<a id="insn-00bbfae4"></a> `00bbfae4` | `09 05 40 39` | ldrb w9,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbfae8"></a> `00bbfae8` | `3f 69 01 71` | cmp w9,#0x5a | `FALL_THROUGH`
<a id="insn-00bbfaec"></a> `00bbfaec` | `41 0a 00 54` | b.ne 0x00bbfc34 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaf0"></a> `00bbfaf0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfaf4"></a> `00bbfaf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfaf8"></a> `00bbfaf8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfafc"></a> `00bbfafc` | `f2 f5 ff 97` | bl 0x00bbd2c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfb00"></a> `00bbfb00` | `60 01 00 b5` | cbnz x0,0x00bbfb2c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb04"></a> `00bbfb04` | `76 00 00 14` | b 0x00bbfcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb08"></a> `00bbfb08` | `7f 15 00 71` | cmp w11,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfb0c"></a> `00bbfb0c` | `20 08 00 54` | b.eq 0x00bbfc10 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb10"></a> `00bbfb10` | `7f 1d 00 71` | cmp w11,#0x7 | `FALL_THROUGH`
<a id="insn-00bbfb14"></a> `00bbfb14` | `c1 13 00 54` | b.ne 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb18"></a> `00bbfb18` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb1c"></a> `00bbfb1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfb20"></a> `00bbfb20` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb24"></a> `00bbfb24` | `e9 0c 00 94` | bl 0x00bc2ec8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfb28"></a> `00bbfb28` | `a0 0d 00 b4` | cbz x0,0x00bbfcdc | `CONDITIONAL_JUMP`
<a id="insn-00bbfb2c"></a> `00bbfb2c` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb30"></a> `00bbfb30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfb34"></a> `00bbfb34` | `e0 08 00 54` | b.eq 0x00bbfc50 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb38"></a> `00bbfb38` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfb3c"></a> `00bbfb3c` | `3f 15 01 71` | cmp w9,#0x45 | `FALL_THROUGH`
<a id="insn-00bbfb40"></a> `00bbfb40` | `81 08 00 54` | b.ne 0x00bbfc50 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb44"></a> `00bbfb44` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb48"></a> `00bbfb48` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb4c"></a> `00bbfb4c` | `64 00 00 14` | b 0x00bbfcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb50"></a> `00bbfb50` | `6b 2a 41 a9` | ldp x11,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfb54"></a> `00bbfb54` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb58"></a> `00bbfb58` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bbfb5c"></a> `00bbfb5c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb60"></a> `00bbfb60` | `4a 01 0b cb` | sub x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbfb64"></a> `00bbfb64` | `54 fd 43 93` | asr x20,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfb68"></a> `00bbfb68` | `0d 00 00 14` | b 0x00bbfb9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb6c"></a> `00bbfb6c` | `a5 75 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfb70"></a> `00bbfb70` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfb74"></a> `00bbfb74` | `a0 11 00 b4` | cbz x0,0x00bbfda8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb78"></a> `00bbfb78` | `c8 fe 42 93` | asr x8,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfb7c"></a> `00bbfb7c` | `17 00 16 8b` | add x23,x0,x22 | `FALL_THROUGH`
<a id="insn-00bbfb80"></a> `00bbfb80` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbfb84"></a> `00bbfb84` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbfb88"></a> `00bbfb88` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfb8c"></a> `00bbfb8c` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfb90"></a> `00bbfb90` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfb94"></a> `00bbfb94` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00bbfb98"></a> `00bbfb98` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb9c"></a> `00bbfb9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfba0"></a> `00bbfba0` | `80 00 00 54` | b.eq 0x00bbfbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfba4"></a> `00bbfba4` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfba8"></a> `00bbfba8` | `3f 15 01 71` | cmp w9,#0x45 | `FALL_THROUGH`
<a id="insn-00bbfbac"></a> `00bbfbac` | `60 05 00 54` | b.eq 0x00bbfc58 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbb0"></a> `00bbfbb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfbb4"></a> `00bbfbb4` | `b6 ff ff 97` | bl 0x00bbfa8c | `UNCONDITIONAL_CALL`
<a id="insn-00bbfbb8"></a> `00bbfbb8` | `20 09 00 b4` | cbz x0,0x00bbfcdc | `CONDITIONAL_JUMP`
<a id="insn-00bbfbbc"></a> `00bbfbbc` | `77 a2 41 a9` | ldp x23,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfbc0"></a> `00bbfbc0` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bbfbc4"></a> `00bbfbc4` | `41 fe ff 54` | b.ne 0x00bbfb8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfbc8"></a> `00bbfbc8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbfbcc"></a> `00bbfbcc` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfbd0"></a> `00bbfbd0` | `f6 02 00 cb` | sub x22,x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfbd4"></a> `00bbfbd4` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00bbfbd8"></a> `00bbfbd8` | `c1 fa 7f d3` | lsl x1,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfbdc"></a> `00bbfbdc` | `81 fc ff 54` | b.ne 0x00bbfb6c | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe0"></a> `00bbfbe0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbfbe4"></a> `00bbfbe4` | `67 75 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfbe8"></a> `00bbfbe8` | `20 0e 00 b4` | cbz x0,0x00bbfdac | `CONDITIONAL_JUMP`
<a id="insn-00bbfbec"></a> `00bbfbec` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00bbfbf0"></a> `00bbfbf0` | `c0 00 00 54` | b.eq 0x00bbfc08 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbf4"></a> `00bbfbf4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbfbf8"></a> `00bbfbf8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbfbfc"></a> `00bbfbfc` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfc00"></a> `00bbfc00` | `58 6d 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfc04"></a> `00bbfc04` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfc08"></a> `00bbfc08` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc0c"></a> `00bbfc0c` | `db ff ff 17` | b 0x00bbfb78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc10"></a> `00bbfc10` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfc14"></a> `00bbfc14` | `c0 0b 00 54` | b.eq 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc18"></a> `00bbfc18` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfc1c"></a> `00bbfc1c` | `3f 51 01 71` | cmp w9,#0x54 | `FALL_THROUGH`
<a id="insn-00bbfc20"></a> `00bbfc20` | `61 0b 00 54` | b.ne 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc24"></a> `00bbfc24` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfc28"></a> `00bbfc28` | `63 06 00 54` | b.cc 0x00bbfcf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc2c"></a> `00bbfc2c` | `01 05 40 39` | ldrb w1,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbfc30"></a> `00bbfc30` | `32 00 00 14` | b 0x00bbfcf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc34"></a> `00bbfc34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfc38"></a> `00bbfc38` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfc3c"></a> `00bbfc3c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfc40"></a> `00bbfc40` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc44"></a> `00bbfc44` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfc48"></a> `00bbfc48` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfc4c"></a> `00bbfc4c` | `14 13 00 14` | b 0x00bc489c | `CALL_TERMINATOR`
<a id="insn-00bbfc50"></a> `00bbfc50` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbfc54"></a> `00bbfc54` | `22 00 00 14` | b 0x00bbfcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc58"></a> `00bbfc58` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc5c"></a> `00bbfc5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfc60"></a> `00bbfc60` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbfc64"></a> `00bbfc64` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfc68"></a> `00bbfc68` | `b1 00 00 94` | bl 0x00bbff2c | `UNCONDITIONAL_CALL`
<a id="insn-00bbfc6c"></a> `00bbfc6c` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfc70"></a> `00bbfc70` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfc74"></a> `00bbfc74` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbfc78"></a> `00bbfc78` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfc7c"></a> `00bbfc7c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfc80"></a> `00bbfc80` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfc84"></a> `00bbfc84` | `08 01 00 54` | b.hi 0x00bbfca4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc88"></a> `00bbfc88` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfc8c"></a> `00bbfc8c` | `3d 75 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfc90"></a> `00bbfc90` | `00 09 00 b4` | cbz x0,0x00bbfdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc94"></a> `00bbfc94` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfc98"></a> `00bbfc98` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfc9c"></a> `00bbfc9c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbfca0"></a> `00bbfca0` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfca4"></a> `00bbfca4` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfca8"></a> `00bbfca8` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbfcac"></a> `00bbfcac` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfcb0"></a> `00bbfcb0` | `08 e1 1e 91` | add x8,x8,#0x7b8 | `FALL_THROUGH`
<a id="insn-00bbfcb4"></a> `00bbfcb4` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfcb8"></a> `00bbfcb8` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bbfcbc"></a> `00bbfcbc` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbfcc0"></a> `00bbfcc0` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfcc4"></a> `00bbfcc4` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbfcc8"></a> `00bbfcc8` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbfccc"></a> `00bbfccc` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfcd0"></a> `00bbfcd0` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbfcd4"></a> `00bbfcd4` | `14 54 01 a9` | stp x20,x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfcd8"></a> `00bbfcd8` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfcdc"></a> `00bbfcdc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfce0"></a> `00bbfce0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfce4"></a> `00bbfce4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfce8"></a> `00bbfce8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfcec"></a> `00bbfcec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfcf0"></a> `00bbfcf0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfcf4"></a> `00bbfcf4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbfcf8"></a> `00bbfcf8` | `b4 b6 ff d0` | adrp x20,0x295000 | `FALL_THROUGH`
<a id="insn-00bbfcfc"></a> `00bbfcfc` | `94 1a 20 91` | add x20,x20,#0x806 | `FALL_THROUGH`
<a id="insn-00bbfd00"></a> `00bbfd00` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfd04"></a> `00bbfd04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfd08"></a> `00bbfd08` | `0a 6d 00 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd0c"></a> `00bbfd0c` | `00 04 00 b4` | cbz x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd10"></a> `00bbfd10` | `08 00 14 cb` | sub x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfd14"></a> `00bbfd14` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd18"></a> `00bbfd18` | `a0 03 00 54` | b.eq 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd1c"></a> `00bbfd1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfd20"></a> `00bbfd20` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbfd24"></a> `00bbfd24` | `17 2b 00 94` | bl 0x00bca980 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd28"></a> `00bbfd28` | `a0 fd ff b4` | cbz x0,0x00bbfcdc | `CONDITIONAL_JUMP`
<a id="insn-00bbfd2c"></a> `00bbfd2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfd30"></a> `00bbfd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfd34"></a> `00bbfd34` | `56 ff ff 97` | bl 0x00bbfa8c | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd38"></a> `00bbfd38` | `20 fd ff b4` | cbz x0,0x00bbfcdc | `CONDITIONAL_JUMP`
<a id="insn-00bbfd3c"></a> `00bbfd3c` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfd40"></a> `00bbfd40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbfd44"></a> `00bbfd44` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd48"></a> `00bbfd48` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfd4c"></a> `00bbfd4c` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfd50"></a> `00bbfd50` | `08 01 00 54` | b.hi 0x00bbfd70 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd54"></a> `00bbfd54` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfd58"></a> `00bbfd58` | `0a 75 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd5c"></a> `00bbfd5c` | `a0 02 00 b4` | cbz x0,0x00bbfdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd60"></a> `00bbfd60` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfd64"></a> `00bbfd64` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfd68"></a> `00bbfd68` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbfd6c"></a> `00bbfd6c` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfd70"></a> `00bbfd70` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfd74"></a> `00bbfd74` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbfd78"></a> `00bbfd78` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfd7c"></a> `00bbfd7c` | `08 a1 20 91` | add x8,x8,#0x828 | `FALL_THROUGH`
<a id="insn-00bbfd80"></a> `00bbfd80` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd84"></a> `00bbfd84` | `49 04 80 52` | mov w9,#0x22 | `FALL_THROUGH`
<a id="insn-00bbfd88"></a> `00bbfd88` | `cd ff ff 17` | b 0x00bbfcbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfd8c"></a> `00bbfd8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfd90"></a> `00bbfd90` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfd94"></a> `00bbfd94` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfd98"></a> `00bbfd98` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfd9c"></a> `00bbfd9c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfda0"></a> `00bbfda0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfda4"></a> `00bbfda4` | `1d f8 ff 17` | b 0x00bbde18 | `CALL_TERMINATOR`
<a id="insn-00bbfda8"></a> `00bbfda8` | `32 79 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bbfdac"></a> `00bbfdac` | `31 79 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bbfdb0"></a> `00bbfdb0` | `f4 6c 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfa8c`](#insn-00bbfa8c) 範囲 `[['00bbfa8c', '00bbfab3']]`
  - `CONDITIONAL_JUMP` [`00bbfab0`](#insn-00bbfab0) → [`00bbfabc`](#insn-00bbfabc)
  - `FALL_THROUGH` [`00bbfab0`](#insn-00bbfab0) → [`00bbfab4`](#insn-00bbfab4)
- ブロック [`00bbfab4`](#insn-00bbfab4) 範囲 `[['00bbfab4', '00bbfabb']]`
  - `UNCONDITIONAL_JUMP` [`00bbfab8`](#insn-00bbfab8) → [`00bbfac0`](#insn-00bbfac0)
- ブロック [`00bbfabc`](#insn-00bbfabc) 範囲 `[['00bbfabc', '00bbfabf']]`
  - `FALL_THROUGH` [`00bbfabc`](#insn-00bbfabc) → [`00bbfac0`](#insn-00bbfac0)
- ブロック [`00bbfac0`](#insn-00bbfac0) 範囲 `[['00bbfac0', '00bbfac7']]`
  - `FALL_THROUGH` [`00bbfac4`](#insn-00bbfac4) → [`00bbfac8`](#insn-00bbfac8)
- ブロック [`00bbfac8`](#insn-00bbfac8) 範囲 `[['00bbfac8', '00bbfacf']]`
  - `CONDITIONAL_JUMP` [`00bbfacc`](#insn-00bbfacc) → [`00bbfb08`](#insn-00bbfb08)
  - `FALL_THROUGH` [`00bbfacc`](#insn-00bbfacc) → [`00bbfad0`](#insn-00bbfad0)
- ブロック [`00bbfad0`](#insn-00bbfad0) 範囲 `[['00bbfad0', '00bbfad3']]`
  - `CONDITIONAL_JUMP` [`00bbfad0`](#insn-00bbfad0) → [`00bbfb50`](#insn-00bbfb50)
  - `FALL_THROUGH` [`00bbfad0`](#insn-00bbfad0) → [`00bbfad4`](#insn-00bbfad4)
- ブロック [`00bbfad4`](#insn-00bbfad4) 範囲 `[['00bbfad4', '00bbfadb']]`
  - `CONDITIONAL_JUMP` [`00bbfad8`](#insn-00bbfad8) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfad8`](#insn-00bbfad8) → [`00bbfadc`](#insn-00bbfadc)
- ブロック [`00bbfadc`](#insn-00bbfadc) 範囲 `[['00bbfadc', '00bbfae3']]`
  - `CONDITIONAL_JUMP` [`00bbfae0`](#insn-00bbfae0) → [`00bbfc34`](#insn-00bbfc34)
  - `FALL_THROUGH` [`00bbfae0`](#insn-00bbfae0) → [`00bbfae4`](#insn-00bbfae4)
- ブロック [`00bbfae4`](#insn-00bbfae4) 範囲 `[['00bbfae4', '00bbfaef']]`
  - `CONDITIONAL_JUMP` [`00bbfaec`](#insn-00bbfaec) → [`00bbfc34`](#insn-00bbfc34)
  - `FALL_THROUGH` [`00bbfaec`](#insn-00bbfaec) → [`00bbfaf0`](#insn-00bbfaf0)
- ブロック [`00bbfaf0`](#insn-00bbfaf0) 範囲 `[['00bbfaf0', '00bbfb03']]`
  - `CONDITIONAL_JUMP` [`00bbfb00`](#insn-00bbfb00) → [`00bbfb2c`](#insn-00bbfb2c)
  - `FALL_THROUGH` [`00bbfb00`](#insn-00bbfb00) → [`00bbfb04`](#insn-00bbfb04)
- ブロック [`00bbfb04`](#insn-00bbfb04) 範囲 `[['00bbfb04', '00bbfb07']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb04`](#insn-00bbfb04) → [`00bbfcdc`](#insn-00bbfcdc)
- ブロック [`00bbfb08`](#insn-00bbfb08) 範囲 `[['00bbfb08', '00bbfb0f']]`
  - `CONDITIONAL_JUMP` [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfc10`](#insn-00bbfc10)
  - `FALL_THROUGH` [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfb10`](#insn-00bbfb10)
- ブロック [`00bbfb10`](#insn-00bbfb10) 範囲 `[['00bbfb10', '00bbfb17']]`
  - `CONDITIONAL_JUMP` [`00bbfb14`](#insn-00bbfb14) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfb14`](#insn-00bbfb14) → [`00bbfb18`](#insn-00bbfb18)
- ブロック [`00bbfb18`](#insn-00bbfb18) 範囲 `[['00bbfb18', '00bbfb2b']]`
  - `CONDITIONAL_JUMP` [`00bbfb28`](#insn-00bbfb28) → [`00bbfcdc`](#insn-00bbfcdc)
  - `FALL_THROUGH` [`00bbfb28`](#insn-00bbfb28) → [`00bbfb2c`](#insn-00bbfb2c)
- ブロック [`00bbfb2c`](#insn-00bbfb2c) 範囲 `[['00bbfb2c', '00bbfb2f']]`
  - `FALL_THROUGH` [`00bbfb2c`](#insn-00bbfb2c) → [`00bbfb30`](#insn-00bbfb30)
- ブロック [`00bbfb30`](#insn-00bbfb30) 範囲 `[['00bbfb30', '00bbfb37']]`
  - `CONDITIONAL_JUMP` [`00bbfb34`](#insn-00bbfb34) → [`00bbfc50`](#insn-00bbfc50)
  - `FALL_THROUGH` [`00bbfb34`](#insn-00bbfb34) → [`00bbfb38`](#insn-00bbfb38)
- ブロック [`00bbfb38`](#insn-00bbfb38) 範囲 `[['00bbfb38', '00bbfb43']]`
  - `CONDITIONAL_JUMP` [`00bbfb40`](#insn-00bbfb40) → [`00bbfc50`](#insn-00bbfc50)
  - `FALL_THROUGH` [`00bbfb40`](#insn-00bbfb40) → [`00bbfb44`](#insn-00bbfb44)
- ブロック [`00bbfb44`](#insn-00bbfb44) 範囲 `[['00bbfb44', '00bbfb4f']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb4c`](#insn-00bbfb4c) → [`00bbfcdc`](#insn-00bbfcdc)
- ブロック [`00bbfb50`](#insn-00bbfb50) 範囲 `[['00bbfb50', '00bbfb6b']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb68`](#insn-00bbfb68) → [`00bbfb9c`](#insn-00bbfb9c)
- ブロック [`00bbfb6c`](#insn-00bbfb6c) 範囲 `[['00bbfb6c', '00bbfb77']]`
  - `CONDITIONAL_JUMP` [`00bbfb74`](#insn-00bbfb74) → [`00bbfda8`](#insn-00bbfda8)
  - `FALL_THROUGH` [`00bbfb74`](#insn-00bbfb74) → [`00bbfb78`](#insn-00bbfb78)
- ブロック [`00bbfb78`](#insn-00bbfb78) 範囲 `[['00bbfb78', '00bbfb8b']]`
  - `FALL_THROUGH` [`00bbfb88`](#insn-00bbfb88) → [`00bbfb8c`](#insn-00bbfb8c)
- ブロック [`00bbfb8c`](#insn-00bbfb8c) 範囲 `[['00bbfb8c', '00bbfb93']]`
  - `FALL_THROUGH` [`00bbfb90`](#insn-00bbfb90) → [`00bbfb94`](#insn-00bbfb94)
- ブロック [`00bbfb94`](#insn-00bbfb94) 範囲 `[['00bbfb94', '00bbfb97']]`
  - `FALL_THROUGH` [`00bbfb94`](#insn-00bbfb94) → [`00bbfb98`](#insn-00bbfb98)
- ブロック [`00bbfb98`](#insn-00bbfb98) 範囲 `[['00bbfb98', '00bbfb9b']]`
  - `FALL_THROUGH` [`00bbfb98`](#insn-00bbfb98) → [`00bbfb9c`](#insn-00bbfb9c)
- ブロック [`00bbfb9c`](#insn-00bbfb9c) 範囲 `[['00bbfb9c', '00bbfba3']]`
  - `CONDITIONAL_JUMP` [`00bbfba0`](#insn-00bbfba0) → [`00bbfbb0`](#insn-00bbfbb0)
  - `FALL_THROUGH` [`00bbfba0`](#insn-00bbfba0) → [`00bbfba4`](#insn-00bbfba4)
- ブロック [`00bbfba4`](#insn-00bbfba4) 範囲 `[['00bbfba4', '00bbfbaf']]`
  - `CONDITIONAL_JUMP` [`00bbfbac`](#insn-00bbfbac) → [`00bbfc58`](#insn-00bbfc58)
  - `FALL_THROUGH` [`00bbfbac`](#insn-00bbfbac) → [`00bbfbb0`](#insn-00bbfbb0)
- ブロック [`00bbfbb0`](#insn-00bbfbb0) 範囲 `[['00bbfbb0', '00bbfbbb']]`
  - `CONDITIONAL_JUMP` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfcdc`](#insn-00bbfcdc)
  - `FALL_THROUGH` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfbbc`](#insn-00bbfbbc)
- ブロック [`00bbfbbc`](#insn-00bbfbbc) 範囲 `[['00bbfbbc', '00bbfbc7']]`
  - `CONDITIONAL_JUMP` [`00bbfbc4`](#insn-00bbfbc4) → [`00bbfb8c`](#insn-00bbfb8c)
  - `FALL_THROUGH` [`00bbfbc4`](#insn-00bbfbc4) → [`00bbfbc8`](#insn-00bbfbc8)
- ブロック [`00bbfbc8`](#insn-00bbfbc8) 範囲 `[['00bbfbc8', '00bbfbdf']]`
  - `CONDITIONAL_JUMP` [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfb6c`](#insn-00bbfb6c)
  - `FALL_THROUGH` [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfbe0`](#insn-00bbfbe0)
- ブロック [`00bbfbe0`](#insn-00bbfbe0) 範囲 `[['00bbfbe0', '00bbfbeb']]`
  - `CONDITIONAL_JUMP` [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfdac`](#insn-00bbfdac)
  - `FALL_THROUGH` [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfbec`](#insn-00bbfbec)
- ブロック [`00bbfbec`](#insn-00bbfbec) 範囲 `[['00bbfbec', '00bbfbf3']]`
  - `CONDITIONAL_JUMP` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc08`](#insn-00bbfc08)
  - `FALL_THROUGH` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfbf4`](#insn-00bbfbf4)
- ブロック [`00bbfbf4`](#insn-00bbfbf4) 範囲 `[['00bbfbf4', '00bbfc07']]`
  - `FALL_THROUGH` [`00bbfc04`](#insn-00bbfc04) → [`00bbfc08`](#insn-00bbfc08)
- ブロック [`00bbfc08`](#insn-00bbfc08) 範囲 `[['00bbfc08', '00bbfc0f']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfb78`](#insn-00bbfb78)
- ブロック [`00bbfc10`](#insn-00bbfc10) 範囲 `[['00bbfc10', '00bbfc17']]`
  - `CONDITIONAL_JUMP` [`00bbfc14`](#insn-00bbfc14) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfc14`](#insn-00bbfc14) → [`00bbfc18`](#insn-00bbfc18)
- ブロック [`00bbfc18`](#insn-00bbfc18) 範囲 `[['00bbfc18', '00bbfc23']]`
  - `CONDITIONAL_JUMP` [`00bbfc20`](#insn-00bbfc20) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfc20`](#insn-00bbfc20) → [`00bbfc24`](#insn-00bbfc24)
- ブロック [`00bbfc24`](#insn-00bbfc24) 範囲 `[['00bbfc24', '00bbfc2b']]`
  - `CONDITIONAL_JUMP` [`00bbfc28`](#insn-00bbfc28) → [`00bbfcf4`](#insn-00bbfcf4)
  - `FALL_THROUGH` [`00bbfc28`](#insn-00bbfc28) → [`00bbfc2c`](#insn-00bbfc2c)
- ブロック [`00bbfc2c`](#insn-00bbfc2c) 範囲 `[['00bbfc2c', '00bbfc33']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc30`](#insn-00bbfc30) → [`00bbfcf8`](#insn-00bbfcf8)
- ブロック [`00bbfc34`](#insn-00bbfc34) 範囲 `[['00bbfc34', '00bbfc4f']]`
- ブロック [`00bbfc50`](#insn-00bbfc50) 範囲 `[['00bbfc50', '00bbfc57']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc54`](#insn-00bbfc54) → [`00bbfcdc`](#insn-00bbfcdc)
- ブロック [`00bbfc58`](#insn-00bbfc58) 範囲 `[['00bbfc58', '00bbfc6f']]`
  - `FALL_THROUGH` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfc70`](#insn-00bbfc70)
- ブロック [`00bbfc70`](#insn-00bbfc70) 範囲 `[['00bbfc70', '00bbfc7b']]`
  - `FALL_THROUGH` [`00bbfc78`](#insn-00bbfc78) → [`00bbfc7c`](#insn-00bbfc7c)
- ブロック [`00bbfc7c`](#insn-00bbfc7c) 範囲 `[['00bbfc7c', '00bbfc87']]`
  - `CONDITIONAL_JUMP` [`00bbfc84`](#insn-00bbfc84) → [`00bbfca4`](#insn-00bbfca4)
  - `FALL_THROUGH` [`00bbfc84`](#insn-00bbfc84) → [`00bbfc88`](#insn-00bbfc88)
- ブロック [`00bbfc88`](#insn-00bbfc88) 範囲 `[['00bbfc88', '00bbfc93']]`
  - `CONDITIONAL_JUMP` [`00bbfc90`](#insn-00bbfc90) → [`00bbfdb0`](#insn-00bbfdb0)
  - `FALL_THROUGH` [`00bbfc90`](#insn-00bbfc90) → [`00bbfc94`](#insn-00bbfc94)
- ブロック [`00bbfc94`](#insn-00bbfc94) 範囲 `[['00bbfc94', '00bbfca3']]`
  - `FALL_THROUGH` [`00bbfca0`](#insn-00bbfca0) → [`00bbfca4`](#insn-00bbfca4)
- ブロック [`00bbfca4`](#insn-00bbfca4) 範囲 `[['00bbfca4', '00bbfcab']]`
  - `FALL_THROUGH` [`00bbfca8`](#insn-00bbfca8) → [`00bbfcac`](#insn-00bbfcac)
- ブロック [`00bbfcac`](#insn-00bbfcac) 範囲 `[['00bbfcac', '00bbfcbb']]`
  - `FALL_THROUGH` [`00bbfcb8`](#insn-00bbfcb8) → [`00bbfcbc`](#insn-00bbfcbc)
- ブロック [`00bbfcbc`](#insn-00bbfcbc) 範囲 `[['00bbfcbc', '00bbfcdb']]`
  - `FALL_THROUGH` [`00bbfcd8`](#insn-00bbfcd8) → [`00bbfcdc`](#insn-00bbfcdc)
- ブロック [`00bbfcdc`](#insn-00bbfcdc) 範囲 `[['00bbfcdc', '00bbfcf3']]`
- ブロック [`00bbfcf4`](#insn-00bbfcf4) 範囲 `[['00bbfcf4', '00bbfcf7']]`
  - `FALL_THROUGH` [`00bbfcf4`](#insn-00bbfcf4) → [`00bbfcf8`](#insn-00bbfcf8)
- ブロック [`00bbfcf8`](#insn-00bbfcf8) 範囲 `[['00bbfcf8', '00bbfd0f']]`
  - `CONDITIONAL_JUMP` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd10`](#insn-00bbfd10)
- ブロック [`00bbfd10`](#insn-00bbfd10) 範囲 `[['00bbfd10', '00bbfd1b']]`
  - `CONDITIONAL_JUMP` [`00bbfd18`](#insn-00bbfd18) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd18`](#insn-00bbfd18) → [`00bbfd1c`](#insn-00bbfd1c)
- ブロック [`00bbfd1c`](#insn-00bbfd1c) 範囲 `[['00bbfd1c', '00bbfd2b']]`
  - `CONDITIONAL_JUMP` [`00bbfd28`](#insn-00bbfd28) → [`00bbfcdc`](#insn-00bbfcdc)
  - `FALL_THROUGH` [`00bbfd28`](#insn-00bbfd28) → [`00bbfd2c`](#insn-00bbfd2c)
- ブロック [`00bbfd2c`](#insn-00bbfd2c) 範囲 `[['00bbfd2c', '00bbfd37']]`
  - `FALL_THROUGH` [`00bbfd34`](#insn-00bbfd34) → [`00bbfd38`](#insn-00bbfd38)
- ブロック [`00bbfd38`](#insn-00bbfd38) 範囲 `[['00bbfd38', '00bbfd3b']]`
  - `CONDITIONAL_JUMP` [`00bbfd38`](#insn-00bbfd38) → [`00bbfcdc`](#insn-00bbfcdc)
  - `FALL_THROUGH` [`00bbfd38`](#insn-00bbfd38) → [`00bbfd3c`](#insn-00bbfd3c)
- ブロック [`00bbfd3c`](#insn-00bbfd3c) 範囲 `[['00bbfd3c', '00bbfd53']]`
  - `CONDITIONAL_JUMP` [`00bbfd50`](#insn-00bbfd50) → [`00bbfd70`](#insn-00bbfd70)
  - `FALL_THROUGH` [`00bbfd50`](#insn-00bbfd50) → [`00bbfd54`](#insn-00bbfd54)
- ブロック [`00bbfd54`](#insn-00bbfd54) 範囲 `[['00bbfd54', '00bbfd5f']]`
  - `CONDITIONAL_JUMP` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfdb0`](#insn-00bbfdb0)
  - `FALL_THROUGH` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfd60`](#insn-00bbfd60)
- ブロック [`00bbfd60`](#insn-00bbfd60) 範囲 `[['00bbfd60', '00bbfd67']]`
  - `FALL_THROUGH` [`00bbfd64`](#insn-00bbfd64) → [`00bbfd68`](#insn-00bbfd68)
- ブロック [`00bbfd68`](#insn-00bbfd68) 範囲 `[['00bbfd68', '00bbfd6f']]`
  - `FALL_THROUGH` [`00bbfd6c`](#insn-00bbfd6c) → [`00bbfd70`](#insn-00bbfd70)
- ブロック [`00bbfd70`](#insn-00bbfd70) 範囲 `[['00bbfd70', '00bbfd8b']]`
  - `UNCONDITIONAL_JUMP` [`00bbfd88`](#insn-00bbfd88) → [`00bbfcbc`](#insn-00bbfcbc)
- ブロック [`00bbfd8c`](#insn-00bbfd8c) 範囲 `[['00bbfd8c', '00bbfda7']]`
- ブロック [`00bbfda8`](#insn-00bbfda8) 範囲 `[['00bbfda8', '00bbfdab']]`
- ブロック [`00bbfdac`](#insn-00bbfdac) 範囲 `[['00bbfdac', '00bbfdaf']]`
- ブロック [`00bbfdb0`](#insn-00bbfdb0) 範囲 `[['00bbfdb0', '00bbfdb3']]`

## 命令位置別の参照

- [`00bbfa90`](#insn-00bbfa90) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa94`](#insn-00bbfa94) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa98`](#insn-00bbfa98) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa9c`](#insn-00bbfa9c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfab0`](#insn-00bbfab0) → [`00bbfabc`](#insn-00bbfabc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfab8`](#insn-00bbfab8) → [`00bbfac0`](#insn-00bbfac0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfacc`](#insn-00bbfacc) → [`00bbfb08`](#insn-00bbfb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfad0`](#insn-00bbfad0) → [`00bbfb50`](#insn-00bbfb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfad8`](#insn-00bbfad8) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfae0`](#insn-00bbfae0) → [`00bbfc34`](#insn-00bbfc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaec`](#insn-00bbfaec) → [`00bbfc34`](#insn-00bbfc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfafc`](#insn-00bbfafc) → [`00bbd2c4`](../00bbd/00bbd2c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd2c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb00`](#insn-00bbfb00) → [`00bbfb2c`](#insn-00bbfb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb04`](#insn-00bbfb04) → [`00bbfcdc`](#insn-00bbfcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb0c`](#insn-00bbfb0c) → [`00bbfc10`](#insn-00bbfc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb14`](#insn-00bbfb14) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb24`](#insn-00bbfb24) → [`00bc2ec8`](../00bc2/00bc2ec8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2ec8` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb28`](#insn-00bbfb28) → [`00bbfcdc`](#insn-00bbfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb34`](#insn-00bbfb34) → [`00bbfc50`](#insn-00bbfc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb40`](#insn-00bbfb40) → [`00bbfc50`](#insn-00bbfc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb4c`](#insn-00bbfb4c) → [`00bbfcdc`](#insn-00bbfcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb68`](#insn-00bbfb68) → [`00bbfb9c`](#insn-00bbfb9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb6c`](#insn-00bbfb6c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb74`](#insn-00bbfb74) → [`00bbfda8`](#insn-00bbfda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfba0`](#insn-00bbfba0) → [`00bbfbb0`](#insn-00bbfbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbac`](#insn-00bbfbac) → [`00bbfc58`](#insn-00bbfc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb4`](#insn-00bbfbb4) → [`00bbfa8c`](#insn-00bbfa8c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfa8c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfcdc`](#insn-00bbfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbc4`](#insn-00bbfbc4) → [`00bbfb8c`](#insn-00bbfb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfb6c`](#insn-00bbfb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe4`](#insn-00bbfbe4) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfdac`](#insn-00bbfdac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc08`](#insn-00bbfc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc00`](#insn-00bbfc00) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfb78`](#insn-00bbfb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc14`](#insn-00bbfc14) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc20`](#insn-00bbfc20) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc28`](#insn-00bbfc28) → [`00bbfcf4`](#insn-00bbfcf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc30`](#insn-00bbfc30) → [`00bbfcf8`](#insn-00bbfcf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc38`](#insn-00bbfc38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc3c`](#insn-00bbfc3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc40`](#insn-00bbfc40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc44`](#insn-00bbfc44) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc4c`](#insn-00bbfc4c) → [`00bc489c`](../00bc4/00bc489c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc489c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc54`](#insn-00bbfc54) → [`00bbfcdc`](#insn-00bbfcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc68`](#insn-00bbfc68) → [`00bbff2c`](00bbff2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbff2c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc84`](#insn-00bbfc84) → [`00bbfca4`](#insn-00bbfca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc8c`](#insn-00bbfc8c) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc90`](#insn-00bbfc90) → [`00bbfdb0`](#insn-00bbfdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcbc`](#insn-00bbfcbc) → `00c197b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbfcbc`](#insn-00bbfcbc) → `00c19828`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbfcdc`](#insn-00bbfcdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfce0`](#insn-00bbfce0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfce4`](#insn-00bbfce4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfce8`](#insn-00bbfce8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd04`](#insn-00bbfd04) → `00295806`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbfd08`](#insn-00bbfd08) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd18`](#insn-00bbfd18) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd24`](#insn-00bbfd24) → [`00bca980`](../00bca/00bca980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bca980` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd28`](#insn-00bbfd28) → [`00bbfcdc`](#insn-00bbfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd34`](#insn-00bbfd34) → [`00bbfa8c`](#insn-00bbfa8c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfa8c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd38`](#insn-00bbfd38) → [`00bbfcdc`](#insn-00bbfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd50`](#insn-00bbfd50) → [`00bbfd70`](#insn-00bbfd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd58`](#insn-00bbfd58) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfdb0`](#insn-00bbfdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd88`](#insn-00bbfd88) → [`00bbfcbc`](#insn-00bbfcbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd90`](#insn-00bbfd90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd94`](#insn-00bbfd94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd98`](#insn-00bbfd98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd9c`](#insn-00bbfd9c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda4`](#insn-00bbfda4) → [`00bbde18`](../00bbd/00bbde18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde18` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda8`](#insn-00bbfda8) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdac`](#insn-00bbfdac) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdb0`](#insn-00bbfdb0) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfa90`](#insn-00bbfa90)

~~~json
{
  "source": "00bbfa90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa94`](#insn-00bbfa94)

~~~json
{
  "source": "00bbfa94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa98`](#insn-00bbfa98)

~~~json
{
  "source": "00bbfa98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa9c`](#insn-00bbfa9c)

~~~json
{
  "source": "00bbfa9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfab0`](#insn-00bbfab0)

~~~json
{
  "source": "00bbfab0",
  "target": "00bbfabc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfab8`](#insn-00bbfab8)

~~~json
{
  "source": "00bbfab8",
  "target": "00bbfac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfacc`](#insn-00bbfacc)

~~~json
{
  "source": "00bbfacc",
  "target": "00bbfb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfad0`](#insn-00bbfad0)

~~~json
{
  "source": "00bbfad0",
  "target": "00bbfb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfad8`](#insn-00bbfad8)

~~~json
{
  "source": "00bbfad8",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfae0`](#insn-00bbfae0)

~~~json
{
  "source": "00bbfae0",
  "target": "00bbfc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaec`](#insn-00bbfaec)

~~~json
{
  "source": "00bbfaec",
  "target": "00bbfc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfafc`](#insn-00bbfafc)

~~~json
{
  "source": "00bbfafc",
  "target": "00bbd2c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb00`](#insn-00bbfb00)

~~~json
{
  "source": "00bbfb00",
  "target": "00bbfb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb04`](#insn-00bbfb04)

~~~json
{
  "source": "00bbfb04",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb0c`](#insn-00bbfb0c)

~~~json
{
  "source": "00bbfb0c",
  "target": "00bbfc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb14`](#insn-00bbfb14)

~~~json
{
  "source": "00bbfb14",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb24`](#insn-00bbfb24)

~~~json
{
  "source": "00bbfb24",
  "target": "00bc2ec8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb28`](#insn-00bbfb28)

~~~json
{
  "source": "00bbfb28",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb34`](#insn-00bbfb34)

~~~json
{
  "source": "00bbfb34",
  "target": "00bbfc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb40`](#insn-00bbfb40)

~~~json
{
  "source": "00bbfb40",
  "target": "00bbfc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb4c`](#insn-00bbfb4c)

~~~json
{
  "source": "00bbfb4c",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb68`](#insn-00bbfb68)

~~~json
{
  "source": "00bbfb68",
  "target": "00bbfb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb6c`](#insn-00bbfb6c)

~~~json
{
  "source": "00bbfb6c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb74`](#insn-00bbfb74)

~~~json
{
  "source": "00bbfb74",
  "target": "00bbfda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfba0`](#insn-00bbfba0)

~~~json
{
  "source": "00bbfba0",
  "target": "00bbfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbac`](#insn-00bbfbac)

~~~json
{
  "source": "00bbfbac",
  "target": "00bbfc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbb4`](#insn-00bbfbb4)

~~~json
{
  "source": "00bbfbb4",
  "target": "00bbfa8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfbb8`](#insn-00bbfbb8)

~~~json
{
  "source": "00bbfbb8",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbc4`](#insn-00bbfbc4)

~~~json
{
  "source": "00bbfbc4",
  "target": "00bbfb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbdc`](#insn-00bbfbdc)

~~~json
{
  "source": "00bbfbdc",
  "target": "00bbfb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbe4`](#insn-00bbfbe4)

~~~json
{
  "source": "00bbfbe4",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfbe8`](#insn-00bbfbe8)

~~~json
{
  "source": "00bbfbe8",
  "target": "00bbfdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf0`](#insn-00bbfbf0)

~~~json
{
  "source": "00bbfbf0",
  "target": "00bbfc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc00`](#insn-00bbfc00)

~~~json
{
  "source": "00bbfc00",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc0c`](#insn-00bbfc0c)

~~~json
{
  "source": "00bbfc0c",
  "target": "00bbfb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc14`](#insn-00bbfc14)

~~~json
{
  "source": "00bbfc14",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc20`](#insn-00bbfc20)

~~~json
{
  "source": "00bbfc20",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc28`](#insn-00bbfc28)

~~~json
{
  "source": "00bbfc28",
  "target": "00bbfcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc30`](#insn-00bbfc30)

~~~json
{
  "source": "00bbfc30",
  "target": "00bbfcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc38`](#insn-00bbfc38)

~~~json
{
  "source": "00bbfc38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc3c`](#insn-00bbfc3c)

~~~json
{
  "source": "00bbfc3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc40`](#insn-00bbfc40)

~~~json
{
  "source": "00bbfc40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc44`](#insn-00bbfc44)

~~~json
{
  "source": "00bbfc44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc4c`](#insn-00bbfc4c)

~~~json
{
  "source": "00bbfc4c",
  "target": "00bc489c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc54`](#insn-00bbfc54)

~~~json
{
  "source": "00bbfc54",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc68`](#insn-00bbfc68)

~~~json
{
  "source": "00bbfc68",
  "target": "00bbff2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc84`](#insn-00bbfc84)

~~~json
{
  "source": "00bbfc84",
  "target": "00bbfca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc8c`](#insn-00bbfc8c)

~~~json
{
  "source": "00bbfc8c",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc90`](#insn-00bbfc90)

~~~json
{
  "source": "00bbfc90",
  "target": "00bbfdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcbc`](#insn-00bbfcbc)

~~~json
{
  "source": "00bbfcbc",
  "target": "00c197b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c197b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbfcbc`](#insn-00bbfcbc)

~~~json
{
  "source": "00bbfcbc",
  "target": "00c19828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbfcdc`](#insn-00bbfcdc)

~~~json
{
  "source": "00bbfcdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfce0`](#insn-00bbfce0)

~~~json
{
  "source": "00bbfce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfce4`](#insn-00bbfce4)

~~~json
{
  "source": "00bbfce4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfce8`](#insn-00bbfce8)

~~~json
{
  "source": "00bbfce8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd04`](#insn-00bbfd04)

~~~json
{
  "source": "00bbfd04",
  "target": "00295806",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295806",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "7970746e6b00",
  "capture_start": "00295806",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbfd08`](#insn-00bbfd08)

~~~json
{
  "source": "00bbfd08",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd0c`](#insn-00bbfd0c)

~~~json
{
  "source": "00bbfd0c",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd18`](#insn-00bbfd18)

~~~json
{
  "source": "00bbfd18",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd24`](#insn-00bbfd24)

~~~json
{
  "source": "00bbfd24",
  "target": "00bca980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd28`](#insn-00bbfd28)

~~~json
{
  "source": "00bbfd28",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd34`](#insn-00bbfd34)

~~~json
{
  "source": "00bbfd34",
  "target": "00bbfa8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd38`](#insn-00bbfd38)

~~~json
{
  "source": "00bbfd38",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd50`](#insn-00bbfd50)

~~~json
{
  "source": "00bbfd50",
  "target": "00bbfd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd58`](#insn-00bbfd58)

~~~json
{
  "source": "00bbfd58",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd5c`](#insn-00bbfd5c)

~~~json
{
  "source": "00bbfd5c",
  "target": "00bbfdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd88`](#insn-00bbfd88)

~~~json
{
  "source": "00bbfd88",
  "target": "00bbfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd90`](#insn-00bbfd90)

~~~json
{
  "source": "00bbfd90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd94`](#insn-00bbfd94)

~~~json
{
  "source": "00bbfd94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd98`](#insn-00bbfd98)

~~~json
{
  "source": "00bbfd98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd9c`](#insn-00bbfd9c)

~~~json
{
  "source": "00bbfd9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfda4`](#insn-00bbfda4)

~~~json
{
  "source": "00bbfda4",
  "target": "00bbde18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfda8`](#insn-00bbfda8)

~~~json
{
  "source": "00bbfda8",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdac`](#insn-00bbfdac)

~~~json
{
  "source": "00bbfdac",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdb0`](#insn-00bbfdb0)

~~~json
{
  "source": "00bbfdb0",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
