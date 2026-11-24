# 00c4cbec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4bbf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0090.md#compare-2cd810341acd88217fe0efd20bd65710)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4cbec",
  "name": "FUN_00c4cbec",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20bbfe82ef11f39122183fb7ab1a479b65dae046791b9f6b9392ae0c5d214ae0",
  "source_text_sha256": "20bbfe82ef11f39122183fb7ab1a479b65dae046791b9f6b9392ae0c5d214ae0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4cbec",
        "00c4cf5f"
      ]
    ],
    "bytes_sha256": "b3b0d160c6103ea33698b8ebbc5e883faabf070d5200fec39c0f0ff864a1c7a6",
    "instruction_count": 221,
    "instruction_bytes": 884,
    "body_bytes": 884,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c403a0](../00c40/00c403a0.md)
- [00c4c83c](../00c4c/00c4c83c.md)

## 呼び出し先

- [00c3bd5c](../00c3b/00c3bd5c.md)
- [00c3f040](../00c3f/00c3f040.md)
- [00c59080](../00c59/00c59080.md)
- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5693 bytes

~~~c

undefined8 * FUN_00c4cbec(long *param_1,undefined1 *param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte bVar4;
  undefined1 uVar5;
  long lVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  size_t sVar9;
  undefined **ppuVar10;
  long lVar11;
  undefined1 uVar12;
  long lVar13;
  ulong uVar14;
  ulong uVar15;
  ulong uVar16;
  char *__s;
  void *pvVar17;
  
  pbVar2 = (byte *)*param_1;
  pbVar3 = (byte *)param_1[1];
  if (1 < (ulong)((long)pbVar3 - (long)pbVar2)) {
    bVar4 = *pbVar2;
    uVar14 = 0;
    uVar15 = 0x3d;
    do {
      uVar16 = uVar14 + uVar15 >> 1;
      if ((byte)(&UNK_00c98820)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else if (((&UNK_00c98820)[uVar16 * 0x10] == bVar4) &&
              ((byte)(&UNK_00c98821)[uVar16 * 0x10] < pbVar2[1])) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
    if (((&UNK_00c98820)[lVar11] == bVar4) && ((&UNK_00c98821)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c98822)[lVar11];
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00c3bd5c();
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00c4cf5c;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c99fc0;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
          *(ushort *)((long)puVar7 + lVar13 + 0x19) =
               *(ushort *)((long)puVar7 + lVar13 + 0x19) & 0xf000 | 0x540;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar5;
        *(char *)(param_1 + 0x61) = (char)lVar11;
        return puVar8;
      }
      if (10 < bVar4) {
        return (undefined8 *)0x0;
      }
      if ((bVar4 == 4) && (((&UNK_00c98823)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c98828 + lVar11);
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00c4cf0c:
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c986e0;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00c4cf0c;
      }
      goto LAB_00c4cf5c;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00c3f040();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00c4cf5c;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c9a030;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00c4ce6c;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00c3f040();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00c4cf5c:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c99fc0;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00c4ce6c:
      *(undefined8 *)(lVar13 + 0x10) = ppuVar10;
      *(undefined1 *)(lVar13 + 0x18) = uVar12;
      *(long *)(lVar13 + 0x20) = lVar11;
      *(ushort *)(lVar13 + 0x19) = *(ushort *)(lVar13 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar13 + 0x10);
    }
  }
  return (undefined8 *)0x0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4cbec"></a> `00c4cbec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4cbf0"></a> `00c4cbf0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00c4cbf4"></a> `00c4cbf4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cbf8"></a> `00c4cbf8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cbfc"></a> `00c4cbfc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c4cc00"></a> `00c4cc00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4cc04"></a> `00c4cc04` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00c4cc08"></a> `00c4cc08` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00c4cc0c"></a> `00c4cc0c` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00c4cc10"></a> `00c4cc10` | `e3 0a 00 54` | b.cc 0x00c4cd6c | `CONDITIONAL_JUMP`
<a id="insn-00c4cc14"></a> `00c4cc14` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00c4cc18"></a> `00c4cc18` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00c4cc1c"></a> `00c4cc1c` | `ad 07 80 52` | mov w13,#0x3d | `FALL_THROUGH`
<a id="insn-00c4cc20"></a> `00c4cc20` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c4cc24"></a> `00c4cc24` | `ec df 25 10` | adr x12,0xc98820 | `FALL_THROUGH`
<a id="insn-00c4cc28"></a> `00c4cc28` | `04 00 00 14` | b 0x00c4cc38 | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cc2c"></a> `00c4cc2c` | `cb 05 00 91` | add x11,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cc30"></a> `00c4cc30` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00c4cc34"></a> `00c4cc34` | `40 02 00 54` | b.eq 0x00c4cc7c | `CONDITIONAL_JUMP`
<a id="insn-00c4cc38"></a> `00c4cc38` | `6e 01 0d 8b` | add x14,x11,x13 | `FALL_THROUGH`
<a id="insn-00c4cc3c"></a> `00c4cc3c` | `ce fd 41 d3` | lsr x14,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cc40"></a> `00c4cc40` | `8f 11 0e 8b` | add x15,x12,x14, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00c4cc44"></a> `00c4cc44` | `f0 01 40 39` | ldrb w16,[x15] | `FALL_THROUGH`
<a id="insn-00c4cc48"></a> `00c4cc48` | `1f 02 0a 6b` | cmp w16,w10 | `FALL_THROUGH`
<a id="insn-00c4cc4c"></a> `00c4cc4c` | `03 ff ff 54` | b.cc 0x00c4cc2c | `CONDITIONAL_JUMP`
<a id="insn-00c4cc50"></a> `00c4cc50` | `21 01 00 54` | b.ne 0x00c4cc74 | `CONDITIONAL_JUMP`
<a id="insn-00c4cc54"></a> `00c4cc54` | `ef 05 40 39` | ldrb w15,[x15, #0x1] | `FALL_THROUGH`
<a id="insn-00c4cc58"></a> `00c4cc58` | `10 05 40 39` | ldrb w16,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00c4cc5c"></a> `00c4cc5c` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00c4cc60"></a> `00c4cc60` | `ef 27 9f 1a` | cset w15,cc | `FALL_THROUGH`
<a id="insn-00c4cc64"></a> `00c4cc64` | `ff 01 00 72` | tst w15,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cc68"></a> `00c4cc68` | `6b 05 8e 9a` | csinc x11,x11,x14,eq | `FALL_THROUGH`
<a id="insn-00c4cc6c"></a> `00c4cc6c` | `ad 11 8e 9a` | csel x13,x13,x14,ne | `FALL_THROUGH`
<a id="insn-00c4cc70"></a> `00c4cc70` | `f0 ff ff 17` | b 0x00c4cc30 | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cc74"></a> `00c4cc74` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00c4cc78"></a> `00c4cc78` | `ee ff ff 17` | b 0x00c4cc30 | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cc7c"></a> `00c4cc7c` | `8b 11 0b 8b` | add x11,x12,x11, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00c4cc80"></a> `00c4cc80` | `6c 01 40 39` | ldrb w12,[x11] | `FALL_THROUGH`
<a id="insn-00c4cc84"></a> `00c4cc84` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00c4cc88"></a> `00c4cc88` | `a1 06 00 54` | b.ne 0x00c4cd5c | `CONDITIONAL_JUMP`
<a id="insn-00c4cc8c"></a> `00c4cc8c` | `6a 05 40 39` | ldrb w10,[x11, #0x1] | `FALL_THROUGH`
<a id="insn-00c4cc90"></a> `00c4cc90` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00c4cc94"></a> `00c4cc94` | `5f 01 0c 6b` | cmp w10,w12 | `FALL_THROUGH`
<a id="insn-00c4cc98"></a> `00c4cc98` | `21 06 00 54` | b.ne 0x00c4cd5c | `CONDITIONAL_JUMP`
<a id="insn-00c4cc9c"></a> `00c4cc9c` | `69 09 40 39` | ldrb w9,[x11, #0x2] | `FALL_THROUGH`
<a id="insn-00c4cca0"></a> `00c4cca0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4cca4"></a> `00c4cca4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00c4cca8"></a> `00c4cca8` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00c4ccac"></a> `00c4ccac` | `21 0f 00 54` | b.ne 0x00c4ce90 | `CONDITIONAL_JUMP`
<a id="insn-00c4ccb0"></a> `00c4ccb0` | `14 24 4c 39` | ldrb w20,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00c4ccb4"></a> `00c4ccb4` | `3f 00 00 f1` | cmp x1,#0x0 | `FALL_THROUGH`
<a id="insn-00c4ccb8"></a> `00c4ccb8` | `15 20 4c 39` | ldrb w21,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00c4ccbc"></a> `00c4ccbc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00c4ccc0"></a> `00c4ccc0` | `1f 20 0c 39` | strb wzr,[x0, #0x308] | `FALL_THROUGH`
<a id="insn-00c4ccc4"></a> `00c4ccc4` | `88 06 9f 1a` | csinc w8,w20,wzr,eq | `FALL_THROUGH`
<a id="insn-00c4ccc8"></a> `00c4ccc8` | `08 24 0c 39` | strb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00c4cccc"></a> `00c4cccc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c4ccd0"></a> `00c4ccd0` | `23 bc ff 97` | bl 0x00c3bd5c | `UNCONDITIONAL_CALL`
<a id="insn-00c4ccd4"></a> `00c4ccd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c4ccd8"></a> `00c4ccd8` | `80 13 00 b4` | cbz x0,0x00c4cf48 | `CONDITIONAL_JUMP`
<a id="insn-00c4ccdc"></a> `00c4ccdc` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00c4cce0"></a> `00c4cce0` | `77 00 00 b4` | cbz x23,0x00c4ccec | `CONDITIONAL_JUMP`
<a id="insn-00c4cce4"></a> `00c4cce4` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cce8"></a> `00c4cce8` | `e9 02 00 39` | strb w9,[x23] | `FALL_THROUGH`
<a id="insn-00c4ccec"></a> `00c4ccec` | `17 99 49 f9` | ldr x23,[x8, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4ccf0"></a> `00c4ccf0` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ccf4"></a> `00c4ccf4` | `2a 41 3f d1` | sub x10,x9,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4ccf8"></a> `00c4ccf8` | `5f c5 3f b1` | cmn x10,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4ccfc"></a> `00c4ccfc` | `28 01 00 54` | b.hi 0x00c4cd20 | `CONDITIONAL_JUMP`
<a id="insn-00c4cd00"></a> `00c4cd00` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4cd04"></a> `00c4cd04` | `ef 38 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4cd08"></a> `00c4cd08` | `a0 12 00 b4` | cbz x0,0x00c4cf5c | `CONDITIONAL_JUMP`
<a id="insn-00c4cd0c"></a> `00c4cd0c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00c4cd10"></a> `00c4cd10` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4cd14"></a> `00c4cd14` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00c4cd18"></a> `00c4cd18` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00c4cd1c"></a> `00c4cd1c` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4cd20"></a> `00c4cd20` | `2a 81 00 91` | add x10,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00c4cd24"></a> `00c4cd24` | `e0 02 09 8b` | add x0,x23,x9 | `FALL_THROUGH`
<a id="insn-00c4cd28"></a> `00c4cd28` | `69 02 00 b0` | adrp x9,0xc99000 | `FALL_THROUGH`
<a id="insn-00c4cd2c"></a> `00c4cd2c` | `29 01 3f 91` | add x9,x9,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c4cd30"></a> `00c4cd30` | `ea 06 00 f9` | str x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cd34"></a> `00c4cd34` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00c4cd38"></a> `00c4cd38` | `09 0c 01 f8` | str x9,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4cd3c"></a> `00c4cd3c` | `09 90 40 78` | ldurh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cd40"></a> `00c4cd40` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00c4cd44"></a> `00c4cd44` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cd48"></a> `00c4cd48` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4cd4c"></a> `00c4cd4c` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cd50"></a> `00c4cd50` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00c4cd54"></a> `00c4cd54` | `09 90 00 78` | sturh w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cd58"></a> `00c4cd58` | `7e 00 00 14` | b 0x00c4cf50 | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cd5c"></a> `00c4cd5c` | `0a 01 40 79` | ldrh w10,[x8] | `FALL_THROUGH`
<a id="insn-00c4cd60"></a> `00c4cd60` | `8b 2d 8d 52` | mov w11,#0x696c | `FALL_THROUGH`
<a id="insn-00c4cd64"></a> `00c4cd64` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00c4cd68"></a> `00c4cd68` | `00 05 00 54` | b.eq 0x00c4ce08 | `CONDITIONAL_JUMP`
<a id="insn-00c4cd6c"></a> `00c4cd6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c4cd70"></a> `00c4cd70` | `40 09 00 54` | b.eq 0x00c4ce98 | `CONDITIONAL_JUMP`
<a id="insn-00c4cd74"></a> `00c4cd74` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00c4cd78"></a> `00c4cd78` | `5f d9 01 71` | cmp w10,#0x76 | `FALL_THROUGH`
<a id="insn-00c4cd7c"></a> `00c4cd7c` | `e1 08 00 54` | b.ne 0x00c4ce98 | `CONDITIONAL_JUMP`
<a id="insn-00c4cd80"></a> `00c4cd80` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cd84"></a> `00c4cd84` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4cd88"></a> `00c4cd88` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00c4cd8c"></a> `00c4cd8c` | `60 08 00 54` | b.eq 0x00c4ce98 | `CONDITIONAL_JUMP`
<a id="insn-00c4cd90"></a> `00c4cd90` | `49 01 40 39` | ldrb w9,[x10] | `FALL_THROUGH`
<a id="insn-00c4cd94"></a> `00c4cd94` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00c4cd98"></a> `00c4cd98` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00c4cd9c"></a> `00c4cd9c` | `e8 07 00 54` | b.hi 0x00c4ce98 | `CONDITIONAL_JUMP`
<a id="insn-00c4cda0"></a> `00c4cda0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4cda4"></a> `00c4cda4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4cda8"></a> `00c4cda8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00c4cdac"></a> `00c4cdac` | `a5 c8 ff 97` | bl 0x00c3f040 | `UNCONDITIONAL_CALL`
<a id="insn-00c4cdb0"></a> `00c4cdb0` | `60 07 00 b4` | cbz x0,0x00c4ce9c | `CONDITIONAL_JUMP`
<a id="insn-00c4cdb4"></a> `00c4cdb4` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4cdb8"></a> `00c4cdb8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00c4cdbc"></a> `00c4cdbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c4cdc0"></a> `00c4cdc0` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cdc4"></a> `00c4cdc4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4cdc8"></a> `00c4cdc8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4cdcc"></a> `00c4cdcc` | `08 01 00 54` | b.hi 0x00c4cdec | `CONDITIONAL_JUMP`
<a id="insn-00c4cdd0"></a> `00c4cdd0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4cdd4"></a> `00c4cdd4` | `bb 38 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4cdd8"></a> `00c4cdd8` | `20 0c 00 b4` | cbz x0,0x00c4cf5c | `CONDITIONAL_JUMP`
<a id="insn-00c4cddc"></a> `00c4cddc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4cde0"></a> `00c4cde0` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4cde4"></a> `00c4cde4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4cde8"></a> `00c4cde8` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4cdec"></a> `00c4cdec` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c4cdf0"></a> `00c4cdf0` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00c4cdf4"></a> `00c4cdf4` | `68 02 00 b0` | adrp x8,0xc99000 | `FALL_THROUGH`
<a id="insn-00c4cdf8"></a> `00c4cdf8` | `08 01 3f 91` | add x8,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c4cdfc"></a> `00c4cdfc` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce00"></a> `00c4ce00` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00c4ce04"></a> `00c4ce04` | `1a 00 00 14` | b 0x00c4ce6c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4ce08"></a> `00c4ce08` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4ce0c"></a> `00c4ce0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4ce10"></a> `00c4ce10` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00c4ce14"></a> `00c4ce14` | `8b c8 ff 97` | bl 0x00c3f040 | `UNCONDITIONAL_CALL`
<a id="insn-00c4ce18"></a> `00c4ce18` | `20 04 00 b4` | cbz x0,0x00c4ce9c | `CONDITIONAL_JUMP`
<a id="insn-00c4ce1c"></a> `00c4ce1c` | `b4 9a 49 f9` | ldr x20,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4ce20"></a> `00c4ce20` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00c4ce24"></a> `00c4ce24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c4ce28"></a> `00c4ce28` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce2c"></a> `00c4ce2c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4ce30"></a> `00c4ce30` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4ce34"></a> `00c4ce34` | `08 01 00 54` | b.hi 0x00c4ce54 | `CONDITIONAL_JUMP`
<a id="insn-00c4ce38"></a> `00c4ce38` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4ce3c"></a> `00c4ce3c` | `a1 38 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4ce40"></a> `00c4ce40` | `e0 08 00 b4` | cbz x0,0x00c4cf5c | `CONDITIONAL_JUMP`
<a id="insn-00c4ce44"></a> `00c4ce44` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4ce48"></a> `00c4ce48` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4ce4c"></a> `00c4ce4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4ce50"></a> `00c4ce50` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4ce54"></a> `00c4ce54` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c4ce58"></a> `00c4ce58` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00c4ce5c"></a> `00c4ce5c` | `68 02 00 d0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00c4ce60"></a> `00c4ce60` | `08 c1 00 91` | add x8,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00c4ce64"></a> `00c4ce64` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce68"></a> `00c4ce68` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-00c4ce6c"></a> `00c4ce6c` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4ce70"></a> `00c4ce70` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ce74"></a> `00c4ce74` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c4ce78"></a> `00c4ce78` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4ce7c"></a> `00c4ce7c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce80"></a> `00c4ce80` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00c4ce84"></a> `00c4ce84` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ce88"></a> `00c4ce88` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ce8c"></a> `00c4ce8c` | `04 00 00 14` | b 0x00c4ce9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4ce90"></a> `00c4ce90` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00c4ce94"></a> `00c4ce94` | `09 01 00 54` | b.ls 0x00c4ceb4 | `CONDITIONAL_JUMP`
<a id="insn-00c4ce98"></a> `00c4ce98` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00c4ce9c"></a> `00c4ce9c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c4cea0"></a> `00c4cea0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cea4"></a> `00c4cea4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cea8"></a> `00c4cea8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00c4ceac"></a> `00c4ceac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ceb0"></a> `00c4ceb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4ceb4"></a> `00c4ceb4` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00c4ceb8"></a> `00c4ceb8` | `61 00 00 54` | b.ne 0x00c4cec4 | `CONDITIONAL_JUMP`
<a id="insn-00c4cebc"></a> `00c4cebc` | `68 0d 40 39` | ldrb w8,[x11, #0x3] | `FALL_THROUGH`
<a id="insn-00c4cec0"></a> `00c4cec0` | `c8 fe 07 36` | tbz w8,#0x0,0x00c4ce98 | `CONDITIONAL_JUMP`
<a id="insn-00c4cec4"></a> `00c4cec4` | `73 05 40 f9` | ldr x19,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cec8"></a> `00c4cec8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4cecc"></a> `00c4cecc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c4ced0"></a> `00c4ced0` | `6c 30 00 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00c4ced4"></a> `00c4ced4` | `95 9a 49 f9` | ldr x21,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4ced8"></a> `00c4ced8` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00c4cedc"></a> `00c4cedc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4cee0"></a> `00c4cee0` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cee4"></a> `00c4cee4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4cee8"></a> `00c4cee8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4ceec"></a> `00c4ceec` | `08 01 00 54` | b.hi 0x00c4cf0c | `CONDITIONAL_JUMP`
<a id="insn-00c4cef0"></a> `00c4cef0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4cef4"></a> `00c4cef4` | `73 38 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4cef8"></a> `00c4cef8` | `20 03 00 b4` | cbz x0,0x00c4cf5c | `CONDITIONAL_JUMP`
<a id="insn-00c4cefc"></a> `00c4cefc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4cf00"></a> `00c4cf00` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4cf04"></a> `00c4cf04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4cf08"></a> `00c4cf08` | `c0 9a 09 f9` | str x0,[x22, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4cf0c"></a> `00c4cf0c` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c4cf10"></a> `00c4cf10` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00c4cf14"></a> `00c4cf14` | `68 02 00 90` | adrp x8,0xc98000 | `FALL_THROUGH`
<a id="insn-00c4cf18"></a> `00c4cf18` | `08 81 1b 91` | add x8,x8,#0x6e0 | `FALL_THROUGH`
<a id="insn-00c4cf1c"></a> `00c4cf1c` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cf20"></a> `00c4cf20` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c4cf24"></a> `00c4cf24` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4cf28"></a> `00c4cf28` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cf2c"></a> `00c4cf2c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00c4cf30"></a> `00c4cf30` | `13 50 01 a9` | stp x19,x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cf34"></a> `00c4cf34` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4cf38"></a> `00c4cf38` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cf3c"></a> `00c4cf3c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00c4cf40"></a> `00c4cf40` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cf44"></a> `00c4cf44` | `d6 ff ff 17` | b 0x00c4ce9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cf48"></a> `00c4cf48` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00c4cf4c"></a> `00c4cf4c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00c4cf50"></a> `00c4cf50` | `14 25 0c 39` | strb w20,[x8, #0x309] | `FALL_THROUGH`
<a id="insn-00c4cf54"></a> `00c4cf54` | `15 21 0c 39` | strb w21,[x8, #0x308] | `FALL_THROUGH`
<a id="insn-00c4cf58"></a> `00c4cf58` | `d1 ff ff 17` | b 0x00c4ce9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4cf5c"></a> `00c4cf5c` | `59 30 00 94` | bl 0x00c590c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4cbec`](#insn-00c4cbec) 範囲 `[['00c4cbec', '00c4cc13']]`
  - `CONDITIONAL_JUMP` [`00c4cc10`](#insn-00c4cc10) → [`00c4cd6c`](#insn-00c4cd6c)
  - `FALL_THROUGH` [`00c4cc10`](#insn-00c4cc10) → [`00c4cc14`](#insn-00c4cc14)
- ブロック [`00c4cc14`](#insn-00c4cc14) 範囲 `[['00c4cc14', '00c4cc2b']]`
  - `UNCONDITIONAL_JUMP` [`00c4cc28`](#insn-00c4cc28) → [`00c4cc38`](#insn-00c4cc38)
- ブロック [`00c4cc2c`](#insn-00c4cc2c) 範囲 `[['00c4cc2c', '00c4cc2f']]`
  - `FALL_THROUGH` [`00c4cc2c`](#insn-00c4cc2c) → [`00c4cc30`](#insn-00c4cc30)
- ブロック [`00c4cc30`](#insn-00c4cc30) 範囲 `[['00c4cc30', '00c4cc37']]`
  - `CONDITIONAL_JUMP` [`00c4cc34`](#insn-00c4cc34) → [`00c4cc7c`](#insn-00c4cc7c)
  - `FALL_THROUGH` [`00c4cc34`](#insn-00c4cc34) → [`00c4cc38`](#insn-00c4cc38)
- ブロック [`00c4cc38`](#insn-00c4cc38) 範囲 `[['00c4cc38', '00c4cc4f']]`
  - `CONDITIONAL_JUMP` [`00c4cc4c`](#insn-00c4cc4c) → [`00c4cc2c`](#insn-00c4cc2c)
  - `FALL_THROUGH` [`00c4cc4c`](#insn-00c4cc4c) → [`00c4cc50`](#insn-00c4cc50)
- ブロック [`00c4cc50`](#insn-00c4cc50) 範囲 `[['00c4cc50', '00c4cc53']]`
  - `CONDITIONAL_JUMP` [`00c4cc50`](#insn-00c4cc50) → [`00c4cc74`](#insn-00c4cc74)
  - `FALL_THROUGH` [`00c4cc50`](#insn-00c4cc50) → [`00c4cc54`](#insn-00c4cc54)
- ブロック [`00c4cc54`](#insn-00c4cc54) 範囲 `[['00c4cc54', '00c4cc73']]`
  - `UNCONDITIONAL_JUMP` [`00c4cc70`](#insn-00c4cc70) → [`00c4cc30`](#insn-00c4cc30)
- ブロック [`00c4cc74`](#insn-00c4cc74) 範囲 `[['00c4cc74', '00c4cc7b']]`
  - `UNCONDITIONAL_JUMP` [`00c4cc78`](#insn-00c4cc78) → [`00c4cc30`](#insn-00c4cc30)
- ブロック [`00c4cc7c`](#insn-00c4cc7c) 範囲 `[['00c4cc7c', '00c4cc8b']]`
  - `CONDITIONAL_JUMP` [`00c4cc88`](#insn-00c4cc88) → [`00c4cd5c`](#insn-00c4cd5c)
  - `FALL_THROUGH` [`00c4cc88`](#insn-00c4cc88) → [`00c4cc8c`](#insn-00c4cc8c)
- ブロック [`00c4cc8c`](#insn-00c4cc8c) 範囲 `[['00c4cc8c', '00c4cc9b']]`
  - `CONDITIONAL_JUMP` [`00c4cc98`](#insn-00c4cc98) → [`00c4cd5c`](#insn-00c4cd5c)
  - `FALL_THROUGH` [`00c4cc98`](#insn-00c4cc98) → [`00c4cc9c`](#insn-00c4cc9c)
- ブロック [`00c4cc9c`](#insn-00c4cc9c) 範囲 `[['00c4cc9c', '00c4ccaf']]`
  - `CONDITIONAL_JUMP` [`00c4ccac`](#insn-00c4ccac) → [`00c4ce90`](#insn-00c4ce90)
  - `FALL_THROUGH` [`00c4ccac`](#insn-00c4ccac) → [`00c4ccb0`](#insn-00c4ccb0)
- ブロック [`00c4ccb0`](#insn-00c4ccb0) 範囲 `[['00c4ccb0', '00c4ccdb']]`
  - `CONDITIONAL_JUMP` [`00c4ccd8`](#insn-00c4ccd8) → [`00c4cf48`](#insn-00c4cf48)
  - `FALL_THROUGH` [`00c4ccd8`](#insn-00c4ccd8) → [`00c4ccdc`](#insn-00c4ccdc)
- ブロック [`00c4ccdc`](#insn-00c4ccdc) 範囲 `[['00c4ccdc', '00c4cce3']]`
  - `CONDITIONAL_JUMP` [`00c4cce0`](#insn-00c4cce0) → [`00c4ccec`](#insn-00c4ccec)
  - `FALL_THROUGH` [`00c4cce0`](#insn-00c4cce0) → [`00c4cce4`](#insn-00c4cce4)
- ブロック [`00c4cce4`](#insn-00c4cce4) 範囲 `[['00c4cce4', '00c4cceb']]`
  - `FALL_THROUGH` [`00c4cce8`](#insn-00c4cce8) → [`00c4ccec`](#insn-00c4ccec)
- ブロック [`00c4ccec`](#insn-00c4ccec) 範囲 `[['00c4ccec', '00c4ccff']]`
  - `CONDITIONAL_JUMP` [`00c4ccfc`](#insn-00c4ccfc) → [`00c4cd20`](#insn-00c4cd20)
  - `FALL_THROUGH` [`00c4ccfc`](#insn-00c4ccfc) → [`00c4cd00`](#insn-00c4cd00)
- ブロック [`00c4cd00`](#insn-00c4cd00) 範囲 `[['00c4cd00', '00c4cd0b']]`
  - `CONDITIONAL_JUMP` [`00c4cd08`](#insn-00c4cd08) → [`00c4cf5c`](#insn-00c4cf5c)
  - `FALL_THROUGH` [`00c4cd08`](#insn-00c4cd08) → [`00c4cd0c`](#insn-00c4cd0c)
- ブロック [`00c4cd0c`](#insn-00c4cd0c) 範囲 `[['00c4cd0c', '00c4cd1f']]`
  - `FALL_THROUGH` [`00c4cd1c`](#insn-00c4cd1c) → [`00c4cd20`](#insn-00c4cd20)
- ブロック [`00c4cd20`](#insn-00c4cd20) 範囲 `[['00c4cd20', '00c4cd5b']]`
  - `UNCONDITIONAL_JUMP` [`00c4cd58`](#insn-00c4cd58) → [`00c4cf50`](#insn-00c4cf50)
- ブロック [`00c4cd5c`](#insn-00c4cd5c) 範囲 `[['00c4cd5c', '00c4cd6b']]`
  - `CONDITIONAL_JUMP` [`00c4cd68`](#insn-00c4cd68) → [`00c4ce08`](#insn-00c4ce08)
  - `FALL_THROUGH` [`00c4cd68`](#insn-00c4cd68) → [`00c4cd6c`](#insn-00c4cd6c)
- ブロック [`00c4cd6c`](#insn-00c4cd6c) 範囲 `[['00c4cd6c', '00c4cd73']]`
  - `CONDITIONAL_JUMP` [`00c4cd70`](#insn-00c4cd70) → [`00c4ce98`](#insn-00c4ce98)
  - `FALL_THROUGH` [`00c4cd70`](#insn-00c4cd70) → [`00c4cd74`](#insn-00c4cd74)
- ブロック [`00c4cd74`](#insn-00c4cd74) 範囲 `[['00c4cd74', '00c4cd7f']]`
  - `CONDITIONAL_JUMP` [`00c4cd7c`](#insn-00c4cd7c) → [`00c4ce98`](#insn-00c4ce98)
  - `FALL_THROUGH` [`00c4cd7c`](#insn-00c4cd7c) → [`00c4cd80`](#insn-00c4cd80)
- ブロック [`00c4cd80`](#insn-00c4cd80) 範囲 `[['00c4cd80', '00c4cd8f']]`
  - `CONDITIONAL_JUMP` [`00c4cd8c`](#insn-00c4cd8c) → [`00c4ce98`](#insn-00c4ce98)
  - `FALL_THROUGH` [`00c4cd8c`](#insn-00c4cd8c) → [`00c4cd90`](#insn-00c4cd90)
- ブロック [`00c4cd90`](#insn-00c4cd90) 範囲 `[['00c4cd90', '00c4cd9f']]`
  - `CONDITIONAL_JUMP` [`00c4cd9c`](#insn-00c4cd9c) → [`00c4ce98`](#insn-00c4ce98)
  - `FALL_THROUGH` [`00c4cd9c`](#insn-00c4cd9c) → [`00c4cda0`](#insn-00c4cda0)
- ブロック [`00c4cda0`](#insn-00c4cda0) 範囲 `[['00c4cda0', '00c4cdb3']]`
  - `CONDITIONAL_JUMP` [`00c4cdb0`](#insn-00c4cdb0) → [`00c4ce9c`](#insn-00c4ce9c)
  - `FALL_THROUGH` [`00c4cdb0`](#insn-00c4cdb0) → [`00c4cdb4`](#insn-00c4cdb4)
- ブロック [`00c4cdb4`](#insn-00c4cdb4) 範囲 `[['00c4cdb4', '00c4cdcf']]`
  - `CONDITIONAL_JUMP` [`00c4cdcc`](#insn-00c4cdcc) → [`00c4cdec`](#insn-00c4cdec)
  - `FALL_THROUGH` [`00c4cdcc`](#insn-00c4cdcc) → [`00c4cdd0`](#insn-00c4cdd0)
- ブロック [`00c4cdd0`](#insn-00c4cdd0) 範囲 `[['00c4cdd0', '00c4cddb']]`
  - `CONDITIONAL_JUMP` [`00c4cdd8`](#insn-00c4cdd8) → [`00c4cf5c`](#insn-00c4cf5c)
  - `FALL_THROUGH` [`00c4cdd8`](#insn-00c4cdd8) → [`00c4cddc`](#insn-00c4cddc)
- ブロック [`00c4cddc`](#insn-00c4cddc) 範囲 `[['00c4cddc', '00c4cdeb']]`
  - `FALL_THROUGH` [`00c4cde8`](#insn-00c4cde8) → [`00c4cdec`](#insn-00c4cdec)
- ブロック [`00c4cdec`](#insn-00c4cdec) 範囲 `[['00c4cdec', '00c4ce07']]`
  - `UNCONDITIONAL_JUMP` [`00c4ce04`](#insn-00c4ce04) → [`00c4ce6c`](#insn-00c4ce6c)
- ブロック [`00c4ce08`](#insn-00c4ce08) 範囲 `[['00c4ce08', '00c4ce1b']]`
  - `CONDITIONAL_JUMP` [`00c4ce18`](#insn-00c4ce18) → [`00c4ce9c`](#insn-00c4ce9c)
  - `FALL_THROUGH` [`00c4ce18`](#insn-00c4ce18) → [`00c4ce1c`](#insn-00c4ce1c)
- ブロック [`00c4ce1c`](#insn-00c4ce1c) 範囲 `[['00c4ce1c', '00c4ce37']]`
  - `CONDITIONAL_JUMP` [`00c4ce34`](#insn-00c4ce34) → [`00c4ce54`](#insn-00c4ce54)
  - `FALL_THROUGH` [`00c4ce34`](#insn-00c4ce34) → [`00c4ce38`](#insn-00c4ce38)
- ブロック [`00c4ce38`](#insn-00c4ce38) 範囲 `[['00c4ce38', '00c4ce43']]`
  - `CONDITIONAL_JUMP` [`00c4ce40`](#insn-00c4ce40) → [`00c4cf5c`](#insn-00c4cf5c)
  - `FALL_THROUGH` [`00c4ce40`](#insn-00c4ce40) → [`00c4ce44`](#insn-00c4ce44)
- ブロック [`00c4ce44`](#insn-00c4ce44) 範囲 `[['00c4ce44', '00c4ce53']]`
  - `FALL_THROUGH` [`00c4ce50`](#insn-00c4ce50) → [`00c4ce54`](#insn-00c4ce54)
- ブロック [`00c4ce54`](#insn-00c4ce54) 範囲 `[['00c4ce54', '00c4ce6b']]`
  - `FALL_THROUGH` [`00c4ce68`](#insn-00c4ce68) → [`00c4ce6c`](#insn-00c4ce6c)
- ブロック [`00c4ce6c`](#insn-00c4ce6c) 範囲 `[['00c4ce6c', '00c4ce8f']]`
  - `UNCONDITIONAL_JUMP` [`00c4ce8c`](#insn-00c4ce8c) → [`00c4ce9c`](#insn-00c4ce9c)
- ブロック [`00c4ce90`](#insn-00c4ce90) 範囲 `[['00c4ce90', '00c4ce97']]`
  - `CONDITIONAL_JUMP` [`00c4ce94`](#insn-00c4ce94) → [`00c4ceb4`](#insn-00c4ceb4)
  - `FALL_THROUGH` [`00c4ce94`](#insn-00c4ce94) → [`00c4ce98`](#insn-00c4ce98)
- ブロック [`00c4ce98`](#insn-00c4ce98) 範囲 `[['00c4ce98', '00c4ce9b']]`
  - `FALL_THROUGH` [`00c4ce98`](#insn-00c4ce98) → [`00c4ce9c`](#insn-00c4ce9c)
- ブロック [`00c4ce9c`](#insn-00c4ce9c) 範囲 `[['00c4ce9c', '00c4ceb3']]`
- ブロック [`00c4ceb4`](#insn-00c4ceb4) 範囲 `[['00c4ceb4', '00c4cebb']]`
  - `CONDITIONAL_JUMP` [`00c4ceb8`](#insn-00c4ceb8) → [`00c4cec4`](#insn-00c4cec4)
  - `FALL_THROUGH` [`00c4ceb8`](#insn-00c4ceb8) → [`00c4cebc`](#insn-00c4cebc)
- ブロック [`00c4cebc`](#insn-00c4cebc) 範囲 `[['00c4cebc', '00c4cec3']]`
  - `CONDITIONAL_JUMP` [`00c4cec0`](#insn-00c4cec0) → [`00c4ce98`](#insn-00c4ce98)
  - `FALL_THROUGH` [`00c4cec0`](#insn-00c4cec0) → [`00c4cec4`](#insn-00c4cec4)
- ブロック [`00c4cec4`](#insn-00c4cec4) 範囲 `[['00c4cec4', '00c4ceef']]`
  - `CONDITIONAL_JUMP` [`00c4ceec`](#insn-00c4ceec) → [`00c4cf0c`](#insn-00c4cf0c)
  - `FALL_THROUGH` [`00c4ceec`](#insn-00c4ceec) → [`00c4cef0`](#insn-00c4cef0)
- ブロック [`00c4cef0`](#insn-00c4cef0) 範囲 `[['00c4cef0', '00c4cefb']]`
  - `CONDITIONAL_JUMP` [`00c4cef8`](#insn-00c4cef8) → [`00c4cf5c`](#insn-00c4cf5c)
  - `FALL_THROUGH` [`00c4cef8`](#insn-00c4cef8) → [`00c4cefc`](#insn-00c4cefc)
- ブロック [`00c4cefc`](#insn-00c4cefc) 範囲 `[['00c4cefc', '00c4cf0b']]`
  - `FALL_THROUGH` [`00c4cf08`](#insn-00c4cf08) → [`00c4cf0c`](#insn-00c4cf0c)
- ブロック [`00c4cf0c`](#insn-00c4cf0c) 範囲 `[['00c4cf0c', '00c4cf47']]`
  - `UNCONDITIONAL_JUMP` [`00c4cf44`](#insn-00c4cf44) → [`00c4ce9c`](#insn-00c4ce9c)
- ブロック [`00c4cf48`](#insn-00c4cf48) 範囲 `[['00c4cf48', '00c4cf4f']]`
  - `FALL_THROUGH` [`00c4cf4c`](#insn-00c4cf4c) → [`00c4cf50`](#insn-00c4cf50)
- ブロック [`00c4cf50`](#insn-00c4cf50) 範囲 `[['00c4cf50', '00c4cf5b']]`
  - `UNCONDITIONAL_JUMP` [`00c4cf58`](#insn-00c4cf58) → [`00c4ce9c`](#insn-00c4ce9c)
- ブロック [`00c4cf5c`](#insn-00c4cf5c) 範囲 `[['00c4cf5c', '00c4cf5f']]`

## 命令位置別の参照

- [`00c4cbf0`](#insn-00c4cbf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbf4`](#insn-00c4cbf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbf8`](#insn-00c4cbf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbfc`](#insn-00c4cbfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc10`](#insn-00c4cc10) → [`00c4cd6c`](#insn-00c4cd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc28`](#insn-00c4cc28) → [`00c4cc38`](#insn-00c4cc38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc34`](#insn-00c4cc34) → [`00c4cc7c`](#insn-00c4cc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc44`](#insn-00c4cc44) → `00c98a00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4cc4c`](#insn-00c4cc4c) → [`00c4cc2c`](#insn-00c4cc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc50`](#insn-00c4cc50) → [`00c4cc74`](#insn-00c4cc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc54`](#insn-00c4cc54) → `00c98a01`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4cc70`](#insn-00c4cc70) → [`00c4cc30`](#insn-00c4cc30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc78`](#insn-00c4cc78) → [`00c4cc30`](#insn-00c4cc30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc80`](#insn-00c4cc80) → `00c98a10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4cc88`](#insn-00c4cc88) → [`00c4cd5c`](#insn-00c4cd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc8c`](#insn-00c4cc8c) → `00c98a11`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4cc98`](#insn-00c4cc98) → [`00c4cd5c`](#insn-00c4cd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cc9c`](#insn-00c4cc9c) → `00c98a12`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4ccac`](#insn-00c4ccac) → [`00c4ce90`](#insn-00c4ce90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ccd0`](#insn-00c4ccd0) → [`00c3bd5c`](../00c3b/00c3bd5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3bd5c` · 推定シンボル `None` · 推定型 `None`
- [`00c4ccd8`](#insn-00c4ccd8) → [`00c4cf48`](#insn-00c4cf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cce0`](#insn-00c4cce0) → [`00c4ccec`](#insn-00c4ccec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ccfc`](#insn-00c4ccfc) → [`00c4cd20`](#insn-00c4cd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd04`](#insn-00c4cd04) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd08`](#insn-00c4cd08) → [`00c4cf5c`](#insn-00c4cf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd38`](#insn-00c4cd38) → `00c99fc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4cd58`](#insn-00c4cd58) → [`00c4cf50`](#insn-00c4cf50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd68`](#insn-00c4cd68) → [`00c4ce08`](#insn-00c4ce08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd70`](#insn-00c4cd70) → [`00c4ce98`](#insn-00c4ce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd7c`](#insn-00c4cd7c) → [`00c4ce98`](#insn-00c4ce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd8c`](#insn-00c4cd8c) → [`00c4ce98`](#insn-00c4ce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cd9c`](#insn-00c4cd9c) → [`00c4ce98`](#insn-00c4ce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdac`](#insn-00c4cdac) → [`00c3f040`](../00c3f/00c3f040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3f040` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdb0`](#insn-00c4cdb0) → [`00c4ce9c`](#insn-00c4ce9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdcc`](#insn-00c4cdcc) → [`00c4cdec`](#insn-00c4cdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdd4`](#insn-00c4cdd4) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdd8`](#insn-00c4cdd8) → [`00c4cf5c`](#insn-00c4cf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce04`](#insn-00c4ce04) → [`00c4ce6c`](#insn-00c4ce6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce14`](#insn-00c4ce14) → [`00c3f040`](../00c3f/00c3f040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3f040` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce18`](#insn-00c4ce18) → [`00c4ce9c`](#insn-00c4ce9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce34`](#insn-00c4ce34) → [`00c4ce54`](#insn-00c4ce54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce3c`](#insn-00c4ce3c) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce40`](#insn-00c4ce40) → [`00c4cf5c`](#insn-00c4cf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce6c`](#insn-00c4ce6c) → `00c99fc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4ce6c`](#insn-00c4ce6c) → `00c9a030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4ce8c`](#insn-00c4ce8c) → [`00c4ce9c`](#insn-00c4ce9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce94`](#insn-00c4ce94) → [`00c4ceb4`](#insn-00c4ceb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce9c`](#insn-00c4ce9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cea0`](#insn-00c4cea0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cea4`](#insn-00c4cea4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cea8`](#insn-00c4cea8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ceb8`](#insn-00c4ceb8) → [`00c4cec4`](#insn-00c4cec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cebc`](#insn-00c4cebc) → `00c98a13`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c4cec0`](#insn-00c4cec0) → [`00c4ce98`](#insn-00c4ce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cec4`](#insn-00c4cec4) → `00c98a18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c4cecc`](#insn-00c4cecc) → `002c2054`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c4ced0`](#insn-00c4ced0) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00c4ceec`](#insn-00c4ceec) → [`00c4cf0c`](#insn-00c4cf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cef4`](#insn-00c4cef4) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c4cef8`](#insn-00c4cef8) → [`00c4cf5c`](#insn-00c4cf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cf24`](#insn-00c4cf24) → `00c986e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4cf30`](#insn-00c4cf30) → `002c2054`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c4cf44`](#insn-00c4cf44) → [`00c4ce9c`](#insn-00c4ce9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cf58`](#insn-00c4cf58) → [`00c4ce9c`](#insn-00c4ce9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cf5c`](#insn-00c4cf5c) → [`00c590c0`](../00c59/00c590c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4cbf0`](#insn-00c4cbf0)

~~~json
{
  "source": "00c4cbf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbf4`](#insn-00c4cbf4)

~~~json
{
  "source": "00c4cbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbf8`](#insn-00c4cbf8)

~~~json
{
  "source": "00c4cbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbfc`](#insn-00c4cbfc)

~~~json
{
  "source": "00c4cbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc10`](#insn-00c4cc10)

~~~json
{
  "source": "00c4cc10",
  "target": "00c4cd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc28`](#insn-00c4cc28)

~~~json
{
  "source": "00c4cc28",
  "target": "00c4cc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc34`](#insn-00c4cc34)

~~~json
{
  "source": "00c4cc34",
  "target": "00c4cc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc44`](#insn-00c4cc44)

~~~json
{
  "source": "00c4cc44",
  "target": "00c98a00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a00",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6c",
  "capture_start": "00c98a00",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cc4c`](#insn-00c4cc4c)

~~~json
{
  "source": "00c4cc4c",
  "target": "00c4cc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc50`](#insn-00c4cc50)

~~~json
{
  "source": "00c4cc50",
  "target": "00c4cc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc54`](#insn-00c4cc54)

~~~json
{
  "source": "00c4cc54",
  "target": "00c98a01",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a01",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "74",
  "capture_start": "00c98a01",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cc70`](#insn-00c4cc70)

~~~json
{
  "source": "00c4cc70",
  "target": "00c4cc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc78`](#insn-00c4cc78)

~~~json
{
  "source": "00c4cc78",
  "target": "00c4cc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc80`](#insn-00c4cc80)

~~~json
{
  "source": "00c4cc80",
  "target": "00c98a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a10",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "6d",
  "capture_start": "00c98a10",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cc88`](#insn-00c4cc88)

~~~json
{
  "source": "00c4cc88",
  "target": "00c4cd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc8c`](#insn-00c4cc8c)

~~~json
{
  "source": "00c4cc8c",
  "target": "00c98a11",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a11",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "49",
  "capture_start": "00c98a11",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cc98`](#insn-00c4cc98)

~~~json
{
  "source": "00c4cc98",
  "target": "00c4cd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cc9c`](#insn-00c4cc9c)

~~~json
{
  "source": "00c4cc9c",
  "target": "00c98a12",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a12",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "02",
  "capture_start": "00c98a12",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4ccac`](#insn-00c4ccac)

~~~json
{
  "source": "00c4ccac",
  "target": "00c4ce90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ccd0`](#insn-00c4ccd0)

~~~json
{
  "source": "00c4ccd0",
  "target": "00c3bd5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ccd8`](#insn-00c4ccd8)

~~~json
{
  "source": "00c4ccd8",
  "target": "00c4cf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cce0`](#insn-00c4cce0)

~~~json
{
  "source": "00c4cce0",
  "target": "00c4ccec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ccfc`](#insn-00c4ccfc)

~~~json
{
  "source": "00c4ccfc",
  "target": "00c4cd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd04`](#insn-00c4cd04)

~~~json
{
  "source": "00c4cd04",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4cd08`](#insn-00c4cd08)

~~~json
{
  "source": "00c4cd08",
  "target": "00c4cf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd38`](#insn-00c4cd38)

~~~json
{
  "source": "00c4cd38",
  "target": "00c99fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4cd58`](#insn-00c4cd58)

~~~json
{
  "source": "00c4cd58",
  "target": "00c4cf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd68`](#insn-00c4cd68)

~~~json
{
  "source": "00c4cd68",
  "target": "00c4ce08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd70`](#insn-00c4cd70)

~~~json
{
  "source": "00c4cd70",
  "target": "00c4ce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd7c`](#insn-00c4cd7c)

~~~json
{
  "source": "00c4cd7c",
  "target": "00c4ce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd8c`](#insn-00c4cd8c)

~~~json
{
  "source": "00c4cd8c",
  "target": "00c4ce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cd9c`](#insn-00c4cd9c)

~~~json
{
  "source": "00c4cd9c",
  "target": "00c4ce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cdac`](#insn-00c4cdac)

~~~json
{
  "source": "00c4cdac",
  "target": "00c3f040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4cdb0`](#insn-00c4cdb0)

~~~json
{
  "source": "00c4cdb0",
  "target": "00c4ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cdcc`](#insn-00c4cdcc)

~~~json
{
  "source": "00c4cdcc",
  "target": "00c4cdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cdd4`](#insn-00c4cdd4)

~~~json
{
  "source": "00c4cdd4",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4cdd8`](#insn-00c4cdd8)

~~~json
{
  "source": "00c4cdd8",
  "target": "00c4cf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce04`](#insn-00c4ce04)

~~~json
{
  "source": "00c4ce04",
  "target": "00c4ce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce14`](#insn-00c4ce14)

~~~json
{
  "source": "00c4ce14",
  "target": "00c3f040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ce18`](#insn-00c4ce18)

~~~json
{
  "source": "00c4ce18",
  "target": "00c4ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce34`](#insn-00c4ce34)

~~~json
{
  "source": "00c4ce34",
  "target": "00c4ce54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce3c`](#insn-00c4ce3c)

~~~json
{
  "source": "00c4ce3c",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ce40`](#insn-00c4ce40)

~~~json
{
  "source": "00c4ce40",
  "target": "00c4cf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce6c`](#insn-00c4ce6c)

~~~json
{
  "source": "00c4ce6c",
  "target": "00c99fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4ce6c`](#insn-00c4ce6c)

~~~json
{
  "source": "00c4ce6c",
  "target": "00c9a030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4ce8c`](#insn-00c4ce8c)

~~~json
{
  "source": "00c4ce8c",
  "target": "00c4ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce94`](#insn-00c4ce94)

~~~json
{
  "source": "00c4ce94",
  "target": "00c4ceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce9c`](#insn-00c4ce9c)

~~~json
{
  "source": "00c4ce9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cea0`](#insn-00c4cea0)

~~~json
{
  "source": "00c4cea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cea4`](#insn-00c4cea4)

~~~json
{
  "source": "00c4cea4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cea8`](#insn-00c4cea8)

~~~json
{
  "source": "00c4cea8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ceb8`](#insn-00c4ceb8)

~~~json
{
  "source": "00c4ceb8",
  "target": "00c4cec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cebc`](#insn-00c4cebc)

~~~json
{
  "source": "00c4cebc",
  "target": "00c98a13",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a13",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "22",
  "capture_start": "00c98a13",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cec0`](#insn-00c4cec0)

~~~json
{
  "source": "00c4cec0",
  "target": "00c4ce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cec4`](#insn-00c4cec4)

~~~json
{
  "source": "00c4cec4",
  "target": "00c98a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c98a18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4cecc`](#insn-00c4cecc)

~~~json
{
  "source": "00c4cecc",
  "target": "002c2054",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c2054",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6f70657261746f722d3d00",
  "capture_start": "002c2054",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4ced0`](#insn-00c4ced0)

~~~json
{
  "source": "00c4ced0",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ceec`](#insn-00c4ceec)

~~~json
{
  "source": "00c4ceec",
  "target": "00c4cf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cef4`](#insn-00c4cef4)

~~~json
{
  "source": "00c4cef4",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4cef8`](#insn-00c4cef8)

~~~json
{
  "source": "00c4cef8",
  "target": "00c4cf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cf24`](#insn-00c4cf24)

~~~json
{
  "source": "00c4cf24",
  "target": "00c986e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c986e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4cf30`](#insn-00c4cf30)

~~~json
{
  "source": "00c4cf30",
  "target": "002c2054",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c2054",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6f70657261746f722d3d00",
  "capture_start": "002c2054",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cf44`](#insn-00c4cf44)

~~~json
{
  "source": "00c4cf44",
  "target": "00c4ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cf58`](#insn-00c4cf58)

~~~json
{
  "source": "00c4cf58",
  "target": "00c4ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cf5c`](#insn-00c4cf5c)

~~~json
{
  "source": "00c4cf5c",
  "target": "00c590c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
