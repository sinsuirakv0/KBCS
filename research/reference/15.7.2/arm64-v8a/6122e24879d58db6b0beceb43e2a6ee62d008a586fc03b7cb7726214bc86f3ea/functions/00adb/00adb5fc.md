# 00adb5fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adb6c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-47cc8c165cb05c36ea5a1b25db1247fd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb5fc",
  "name": "FUN_00adb5fc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0acf86c1db9ab749b5b1b701ac120fcac3ef743f0ff886d3ce087d9dc21b4454",
  "source_text_sha256": "0acf86c1db9ab749b5b1b701ac120fcac3ef743f0ff886d3ce087d9dc21b4454",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb5fc",
        "00adb6ff"
      ]
    ],
    "bytes_sha256": "884e465a8f11bf1183ceee4c3c11e942d5239a484d7511b3b3e877e091c25188",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adb4c4](../00adb/00adb4c4.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1890 bytes

~~~c

long * FUN_00adb5fc(long param_1,undefined8 *param_2,byte *param_3)

{
  void *__s2;
  size_t __n;
  ulong uVar1;
  byte *__s1;
  bool bVar2;
  ulong uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = (long *)(param_1 + 8);
  plVar5 = (long *)*plVar6;
  plVar7 = plVar6;
  if (plVar5 != (long *)0x0) {
    uVar1 = *(ulong *)(param_3 + 8);
    __s1 = *(byte **)(param_3 + 0x10);
    if ((*param_3 & 1) == 0) {
      __s1 = param_3 + 1;
      uVar1 = (ulong)(*param_3 >> 1);
    }
    do {
      while( true ) {
        plVar7 = plVar5;
                    /* try { // try from 00adb65c to 00bdb663 has its CatchHandler @ 00adb8dc */
                    /* try { // try from 00adb664 to 00bdb6b7 has its CatchHandler @ 00adafd0 */
        __s2 = (void *)((long)plVar7 + 0x21);
        uVar3 = (ulong)(*(byte *)(plVar7 + 4) >> 1);
        if ((*(byte *)(plVar7 + 4) & 1) != 0) {
          __s2 = (void *)plVar7[6];
          uVar3 = plVar7[5];
        }
        __n = uVar3;
        if (uVar1 <= uVar3) {
          __n = uVar1;
        }
        iVar4 = memcmp(__s1,__s2,__n);
        bVar2 = uVar1 < uVar3;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (bVar2) break;
        iVar4 = memcmp(__s2,__s1,__n);
                    /* try { // try from 00adb6b8 to 00bdb6c3 has its CatchHandler @ 00adb9b4 */
        bVar2 = uVar3 < uVar1;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
                    /* try { // try from 00adb6c4 to 00bdba33 has its CatchHandler @ 00adafd0 */
        if (!bVar2) goto LAB_00adb6e0;
        plVar6 = plVar7 + 1;
        plVar5 = (long *)*plVar6;
        if ((long *)*plVar6 == (long *)0x0) goto LAB_00adb6e0;
      }
      plVar5 = (long *)*plVar7;
      plVar6 = plVar7;
    } while ((long *)*plVar7 != (long *)0x0);
  }
LAB_00adb6e0:
  *param_2 = plVar7;
  return plVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adb5fc"></a> `00adb5fc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adb600"></a> `00adb600` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb604"></a> `00adb604` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb608"></a> `00adb608` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb60c"></a> `00adb60c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb610"></a> `00adb610` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adb614"></a> `00adb614` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adb618"></a> `00adb618` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00adb61c"></a> `00adb61c` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00adb620"></a> `00adb620` | `e8 05 00 b4` | cbz x8,0x00adb6dc | `CONDITIONAL_JUMP`
<a id="insn-00adb624"></a> `00adb624` | `49 00 40 39` | ldrb w9,[x2] | `FALL_THROUGH`
<a id="insn-00adb628"></a> `00adb628` | `4b b0 40 a9` | ldp x11,x12,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00adb62c"></a> `00adb62c` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00adb630"></a> `00adb630` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adb634"></a> `00adb634` | `95 15 82 9a` | csinc x21,x12,x2,ne | `FALL_THROUGH`
<a id="insn-00adb638"></a> `00adb638` | `59 01 8b 9a` | csel x25,x10,x11,eq | `FALL_THROUGH`
<a id="insn-00adb63c"></a> `00adb63c` | `04 00 00 14` | b 0x00adb64c | `UNCONDITIONAL_JUMP`
<a id="insn-00adb640"></a> `00adb640` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adb644"></a> `00adb644` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00adb648"></a> `00adb648` | `c8 04 00 b4` | cbz x8,0x00adb6e0 | `CONDITIONAL_JUMP`
<a id="insn-00adb64c"></a> `00adb64c` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00adb650"></a> `00adb650` | `08 81 40 39` | ldrb w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb654"></a> `00adb654` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00adb658"></a> `00adb658` | `09 af 42 a9` | ldp x9,x11,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00adb65c"></a> `00adb65c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb660"></a> `00adb660` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb664"></a> `00adb664` | `08 87 00 91` | add x8,x24,#0x21 | `FALL_THROUGH`
<a id="insn-00adb668"></a> `00adb668` | `5a 01 89 9a` | csel x26,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00adb66c"></a> `00adb66c` | `16 01 8b 9a` | csel x22,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00adb670"></a> `00adb670` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00adb674"></a> `00adb674` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00adb678"></a> `00adb678` | `57 33 99 9a` | csel x23,x26,x25,cc | `FALL_THROUGH`
<a id="insn-00adb67c"></a> `00adb67c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00adb680"></a> `00adb680` | `a0 fe 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00adb684"></a> `00adb684` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00adb688"></a> `00adb688` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adb68c"></a> `00adb68c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adb690"></a> `00adb690` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adb694"></a> `00adb694` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adb698"></a> `00adb698` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb69c"></a> `00adb69c` | `20 fd ff 54` | b.eq 0x00adb640 | `CONDITIONAL_JUMP`
<a id="insn-00adb6a0"></a> `00adb6a0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00adb6a4"></a> `00adb6a4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adb6a8"></a> `00adb6a8` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00adb6ac"></a> `00adb6ac` | `95 fe 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00adb6b0"></a> `00adb6b0` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00adb6b4"></a> `00adb6b4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adb6b8"></a> `00adb6b8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adb6bc"></a> `00adb6bc` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adb6c0"></a> `00adb6c0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adb6c4"></a> `00adb6c4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb6c8"></a> `00adb6c8` | `c1 00 00 54` | b.ne 0x00adb6e0 | `CONDITIONAL_JUMP`
<a id="insn-00adb6cc"></a> `00adb6cc` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00adb6d0"></a> `00adb6d0` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00adb6d4"></a> `00adb6d4` | `c8 fb ff b5` | cbnz x8,0x00adb64c | `CONDITIONAL_JUMP`
<a id="insn-00adb6d8"></a> `00adb6d8` | `02 00 00 14` | b 0x00adb6e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb6dc"></a> `00adb6dc` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00adb6e0"></a> `00adb6e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb6e4"></a> `00adb6e4` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00adb6e8"></a> `00adb6e8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb6ec"></a> `00adb6ec` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb6f0"></a> `00adb6f0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb6f4"></a> `00adb6f4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb6f8"></a> `00adb6f8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adb6fc"></a> `00adb6fc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb5fc`](#insn-00adb5fc) 範囲 `[['00adb5fc', '00adb623']]`
  - `CONDITIONAL_JUMP` [`00adb620`](#insn-00adb620) → [`00adb6dc`](#insn-00adb6dc)
  - `FALL_THROUGH` [`00adb620`](#insn-00adb620) → [`00adb624`](#insn-00adb624)
- ブロック [`00adb624`](#insn-00adb624) 範囲 `[['00adb624', '00adb63f']]`
  - `UNCONDITIONAL_JUMP` [`00adb63c`](#insn-00adb63c) → [`00adb64c`](#insn-00adb64c)
- ブロック [`00adb640`](#insn-00adb640) 範囲 `[['00adb640', '00adb64b']]`
  - `CONDITIONAL_JUMP` [`00adb648`](#insn-00adb648) → [`00adb6e0`](#insn-00adb6e0)
  - `FALL_THROUGH` [`00adb648`](#insn-00adb648) → [`00adb64c`](#insn-00adb64c)
- ブロック [`00adb64c`](#insn-00adb64c) 範囲 `[['00adb64c', '00adb65b']]`
  - `FALL_THROUGH` [`00adb658`](#insn-00adb658) → [`00adb65c`](#insn-00adb65c)
- ブロック [`00adb65c`](#insn-00adb65c) 範囲 `[['00adb65c', '00adb663']]`
  - `FALL_THROUGH` [`00adb660`](#insn-00adb660) → [`00adb664`](#insn-00adb664)
- ブロック [`00adb664`](#insn-00adb664) 範囲 `[['00adb664', '00adb69f']]`
  - `CONDITIONAL_JUMP` [`00adb69c`](#insn-00adb69c) → [`00adb640`](#insn-00adb640)
  - `FALL_THROUGH` [`00adb69c`](#insn-00adb69c) → [`00adb6a0`](#insn-00adb6a0)
- ブロック [`00adb6a0`](#insn-00adb6a0) 範囲 `[['00adb6a0', '00adb6b7']]`
  - `FALL_THROUGH` [`00adb6b4`](#insn-00adb6b4) → [`00adb6b8`](#insn-00adb6b8)
- ブロック [`00adb6b8`](#insn-00adb6b8) 範囲 `[['00adb6b8', '00adb6c3']]`
  - `FALL_THROUGH` [`00adb6c0`](#insn-00adb6c0) → [`00adb6c4`](#insn-00adb6c4)
- ブロック [`00adb6c4`](#insn-00adb6c4) 範囲 `[['00adb6c4', '00adb6cb']]`
  - `CONDITIONAL_JUMP` [`00adb6c8`](#insn-00adb6c8) → [`00adb6e0`](#insn-00adb6e0)
  - `FALL_THROUGH` [`00adb6c8`](#insn-00adb6c8) → [`00adb6cc`](#insn-00adb6cc)
- ブロック [`00adb6cc`](#insn-00adb6cc) 範囲 `[['00adb6cc', '00adb6d7']]`
  - `CONDITIONAL_JUMP` [`00adb6d4`](#insn-00adb6d4) → [`00adb64c`](#insn-00adb64c)
  - `FALL_THROUGH` [`00adb6d4`](#insn-00adb6d4) → [`00adb6d8`](#insn-00adb6d8)
- ブロック [`00adb6d8`](#insn-00adb6d8) 範囲 `[['00adb6d8', '00adb6db']]`
  - `UNCONDITIONAL_JUMP` [`00adb6d8`](#insn-00adb6d8) → [`00adb6e0`](#insn-00adb6e0)
- ブロック [`00adb6dc`](#insn-00adb6dc) 範囲 `[['00adb6dc', '00adb6df']]`
  - `FALL_THROUGH` [`00adb6dc`](#insn-00adb6dc) → [`00adb6e0`](#insn-00adb6e0)
- ブロック [`00adb6e0`](#insn-00adb6e0) 範囲 `[['00adb6e0', '00adb6ff']]`

## 命令位置別の参照

- [`00adb5fc`](#insn-00adb5fc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb600`](#insn-00adb600) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb604`](#insn-00adb604) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb608`](#insn-00adb608) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb60c`](#insn-00adb60c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb620`](#insn-00adb620) → [`00adb6dc`](#insn-00adb6dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb63c`](#insn-00adb63c) → [`00adb64c`](#insn-00adb64c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb648`](#insn-00adb648) → [`00adb6e0`](#insn-00adb6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb680`](#insn-00adb680) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00adb69c`](#insn-00adb69c) → [`00adb640`](#insn-00adb640) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6ac`](#insn-00adb6ac) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00adb6c8`](#insn-00adb6c8) → [`00adb6e0`](#insn-00adb6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6d4`](#insn-00adb6d4) → [`00adb64c`](#insn-00adb64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6d8`](#insn-00adb6d8) → [`00adb6e0`](#insn-00adb6e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6e8`](#insn-00adb6e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6ec`](#insn-00adb6ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6f0`](#insn-00adb6f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6f4`](#insn-00adb6f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb6f8`](#insn-00adb6f8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb5fc`](#insn-00adb5fc)

~~~json
{
  "source": "00adb5fc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb600`](#insn-00adb600)

~~~json
{
  "source": "00adb600",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb604`](#insn-00adb604)

~~~json
{
  "source": "00adb604",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb608`](#insn-00adb608)

~~~json
{
  "source": "00adb608",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb60c`](#insn-00adb60c)

~~~json
{
  "source": "00adb60c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb620`](#insn-00adb620)

~~~json
{
  "source": "00adb620",
  "target": "00adb6dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb63c`](#insn-00adb63c)

~~~json
{
  "source": "00adb63c",
  "target": "00adb64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb648`](#insn-00adb648)

~~~json
{
  "source": "00adb648",
  "target": "00adb6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb680`](#insn-00adb680)

~~~json
{
  "source": "00adb680",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb69c`](#insn-00adb69c)

~~~json
{
  "source": "00adb69c",
  "target": "00adb640",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6ac`](#insn-00adb6ac)

~~~json
{
  "source": "00adb6ac",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb6c8`](#insn-00adb6c8)

~~~json
{
  "source": "00adb6c8",
  "target": "00adb6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6d4`](#insn-00adb6d4)

~~~json
{
  "source": "00adb6d4",
  "target": "00adb64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6d8`](#insn-00adb6d8)

~~~json
{
  "source": "00adb6d8",
  "target": "00adb6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6e8`](#insn-00adb6e8)

~~~json
{
  "source": "00adb6e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6ec`](#insn-00adb6ec)

~~~json
{
  "source": "00adb6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6f0`](#insn-00adb6f0)

~~~json
{
  "source": "00adb6f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6f4`](#insn-00adb6f4)

~~~json
{
  "source": "00adb6f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb6f8`](#insn-00adb6f8)

~~~json
{
  "source": "00adb6f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
