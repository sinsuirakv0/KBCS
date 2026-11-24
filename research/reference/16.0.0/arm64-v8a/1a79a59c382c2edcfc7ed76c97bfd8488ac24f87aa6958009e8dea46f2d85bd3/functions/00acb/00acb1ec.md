# 00acb1ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-79ba57428635718f2cc74656b9b4ec25)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb3e8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb3e8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-96cd8c7cc7c5e110499649a5fc456d6d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acb1ec",
  "name": "FUN_00acb1ec",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf71fced50f5d714c9f67dba176312a2c4dc82a46487ac97b08c9ad5f26ead84",
  "source_text_sha256": "bf71fced50f5d714c9f67dba176312a2c4dc82a46487ac97b08c9ad5f26ead84",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acb1ec",
        "00acb2e7"
      ]
    ],
    "bytes_sha256": "b3b8524d8c664e827e1ccf6968e130985b435a95e5d4c6493b74ff04e7b5c6cc",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459d34](../00459/00459d34.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008514b8](../00851/008514b8.md)
- [008b6e60](../008b6/008b6e60.md)
- [00a466e0](../00a46/00a466e0.md)
- [00a466f8](../00a46/00a466f8.md)
- [00a469c0](../00a46/00a469c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1433 bytes

~~~c

void FUN_00acb1ec(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  uint uVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  
  uVar7 = *param_2;
  iVar3 = *param_3;
  uVar4 = FUN_008b6e60(uVar7);
  uVar4 = FUN_00a466f8(uVar4,1);
  if (iVar3 == 2) {
    lVar5 = FUN_008514b8();
    iVar3 = *(int *)((long)&fde_table_entry_00337d90.initial_loc + lVar5);
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    uVar1 = iVar3 >> 1 & 1;
    uVar2 = -uVar1;
    if (-1 < iVar3 >> 1) {
      uVar2 = uVar1;
    }
    FUN_00a469c0(uVar4,uVar2 + 0xc);
    uVar4 = FUN_008b6e60(uVar7);
    uVar4 = FUN_00a466f8(uVar4,1);
    FUN_00a466e0(uVar4,1);
    return;
  }
  FUN_00a466e0(uVar4,0);
  if (iVar3 != 4) {
    if (iVar3 == 3) {
      uVar4 = FUN_0047acb4();
      uVar7 = 0xb;
    }
    else {
      if (iVar3 != 0) {
        return;
      }
      uVar4 = FUN_0047acb4();
      uVar7 = 10;
    }
    FUN_0047cd94(uVar4,uVar7,0);
    return;
  }
  lVar5 = FUN_008514b8();
  plVar6 = *(long **)((long)&fde_table_entry_00337e60.initial_loc + lVar5);
  if (plVar6 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00acb2d4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar6 + 0x30))();
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00459d34();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acb1ec"></a> `00acb1ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acb1f0"></a> `00acb1f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1f4"></a> `00acb1f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acb1f8"></a> `00acb1f8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00acb1fc"></a> `00acb1fc` | `54 00 40 b9` | ldr w20,[x2] | `FALL_THROUGH`
<a id="insn-00acb200"></a> `00acb200` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb204"></a> `00acb204` | `17 af f7 97` | bl 0x008b6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00acb208"></a> `00acb208` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acb20c"></a> `00acb20c` | `3b ed fd 97` | bl 0x00a466f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb210"></a> `00acb210` | `9f 0a 00 71` | cmp w20,#0x2 | `FALL_THROUGH`
<a id="insn-00acb214"></a> `00acb214` | `e1 02 00 54` | b.ne 0x00acb270 | `CONDITIONAL_JUMP`
<a id="insn-00acb218"></a> `00acb218` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acb21c"></a> `00acb21c` | `a7 18 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb220"></a> `00acb220` | `08 b2 8f 52` | mov w8,#0x7d90 | `FALL_THROUGH`
<a id="insn-00acb224"></a> `00acb224` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb228"></a> `00acb228` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb22c"></a> `00acb22c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb230"></a> `00acb230` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00acb234"></a> `00acb234` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00acb238"></a> `00acb238` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acb23c"></a> `00acb23c` | `09 01 00 12` | and w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acb240"></a> `00acb240` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00acb244"></a> `00acb244` | `28 a5 89 5a` | cneg w8,w9,lt | `FALL_THROUGH`
<a id="insn-00acb248"></a> `00acb248` | `01 31 00 11` | add w1,w8,#0xc | `FALL_THROUGH`
<a id="insn-00acb24c"></a> `00acb24c` | `dd ed fd 97` | bl 0x00a469c0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb250"></a> `00acb250` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb254"></a> `00acb254` | `03 af f7 97` | bl 0x008b6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00acb258"></a> `00acb258` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acb25c"></a> `00acb25c` | `27 ed fd 97` | bl 0x00a466f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb260"></a> `00acb260` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acb264"></a> `00acb264` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb268"></a> `00acb268` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb26c"></a> `00acb26c` | `1d ed fd 17` | b 0x00a466e0 | `CALL_TERMINATOR`
<a id="insn-00acb270"></a> `00acb270` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acb274"></a> `00acb274` | `1b ed fd 97` | bl 0x00a466e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb278"></a> `00acb278` | `9f 12 00 71` | cmp w20,#0x4 | `FALL_THROUGH`
<a id="insn-00acb27c"></a> `00acb27c` | `a0 01 00 54` | b.eq 0x00acb2b0 | `CONDITIONAL_JUMP`
<a id="insn-00acb280"></a> `00acb280` | `9f 0e 00 71` | cmp w20,#0x3 | `FALL_THROUGH`
<a id="insn-00acb284"></a> `00acb284` | `a0 00 00 54` | b.eq 0x00acb298 | `CONDITIONAL_JUMP`
<a id="insn-00acb288"></a> `00acb288` | `94 02 00 35` | cbnz w20,0x00acb2d8 | `CONDITIONAL_JUMP`
<a id="insn-00acb28c"></a> `00acb28c` | `8a be e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00acb290"></a> `00acb290` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00acb294"></a> `00acb294` | `03 00 00 14` | b 0x00acb2a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb298"></a> `00acb298` | `87 be e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00acb29c"></a> `00acb29c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00acb2a0"></a> `00acb2a0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00acb2a4"></a> `00acb2a4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb2a8"></a> `00acb2a8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb2ac"></a> `00acb2ac` | `ba c6 e6 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00acb2b0"></a> `00acb2b0` | `82 18 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb2b4"></a> `00acb2b4` | `08 cc 8f 52` | mov w8,#0x7e60 | `FALL_THROUGH`
<a id="insn-00acb2b8"></a> `00acb2b8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acb2bc"></a> `00acb2bc` | `00 68 68 f8` | ldr x0,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb2c0"></a> `00acb2c0` | `20 01 00 b4` | cbz x0,0x00acb2e4 | `CONDITIONAL_JUMP`
<a id="insn-00acb2c4"></a> `00acb2c4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acb2c8"></a> `00acb2c8` | `01 19 40 f9` | ldr x1,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00acb2cc"></a> `00acb2cc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb2d0"></a> `00acb2d0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb2d4"></a> `00acb2d4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00acb2d8"></a> `00acb2d8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb2dc"></a> `00acb2dc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb2e0"></a> `00acb2e0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acb2e4"></a> `00acb2e4` | `94 3a e6 97` | bl 0x00459d34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acb1ec`](#insn-00acb1ec) 範囲 `[['00acb1ec', '00acb217']]`
  - `CONDITIONAL_JUMP` [`00acb214`](#insn-00acb214) → [`00acb270`](#insn-00acb270)
  - `FALL_THROUGH` [`00acb214`](#insn-00acb214) → [`00acb218`](#insn-00acb218)
- ブロック [`00acb218`](#insn-00acb218) 範囲 `[['00acb218', '00acb26f']]`
- ブロック [`00acb270`](#insn-00acb270) 範囲 `[['00acb270', '00acb27f']]`
  - `CONDITIONAL_JUMP` [`00acb27c`](#insn-00acb27c) → [`00acb2b0`](#insn-00acb2b0)
  - `FALL_THROUGH` [`00acb27c`](#insn-00acb27c) → [`00acb280`](#insn-00acb280)
- ブロック [`00acb280`](#insn-00acb280) 範囲 `[['00acb280', '00acb287']]`
  - `CONDITIONAL_JUMP` [`00acb284`](#insn-00acb284) → [`00acb298`](#insn-00acb298)
  - `FALL_THROUGH` [`00acb284`](#insn-00acb284) → [`00acb288`](#insn-00acb288)
- ブロック [`00acb288`](#insn-00acb288) 範囲 `[['00acb288', '00acb28b']]`
  - `CONDITIONAL_JUMP` [`00acb288`](#insn-00acb288) → [`00acb2d8`](#insn-00acb2d8)
  - `FALL_THROUGH` [`00acb288`](#insn-00acb288) → [`00acb28c`](#insn-00acb28c)
- ブロック [`00acb28c`](#insn-00acb28c) 範囲 `[['00acb28c', '00acb297']]`
  - `UNCONDITIONAL_JUMP` [`00acb294`](#insn-00acb294) → [`00acb2a0`](#insn-00acb2a0)
- ブロック [`00acb298`](#insn-00acb298) 範囲 `[['00acb298', '00acb29f']]`
  - `FALL_THROUGH` [`00acb29c`](#insn-00acb29c) → [`00acb2a0`](#insn-00acb2a0)
- ブロック [`00acb2a0`](#insn-00acb2a0) 範囲 `[['00acb2a0', '00acb2af']]`
- ブロック [`00acb2b0`](#insn-00acb2b0) 範囲 `[['00acb2b0', '00acb2c3']]`
  - `CONDITIONAL_JUMP` [`00acb2c0`](#insn-00acb2c0) → [`00acb2e4`](#insn-00acb2e4)
  - `FALL_THROUGH` [`00acb2c0`](#insn-00acb2c0) → [`00acb2c4`](#insn-00acb2c4)
- ブロック [`00acb2c4`](#insn-00acb2c4) 範囲 `[['00acb2c4', '00acb2d7']]`
- ブロック [`00acb2d8`](#insn-00acb2d8) 範囲 `[['00acb2d8', '00acb2e3']]`
- ブロック [`00acb2e4`](#insn-00acb2e4) 範囲 `[['00acb2e4', '00acb2e7']]`

## 命令位置別の参照

- [`00acb1ec`](#insn-00acb1ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1f0`](#insn-00acb1f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb204`](#insn-00acb204) → [`008b6e60`](../008b6/008b6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6e60` · 推定シンボル `None` · 推定型 `None`
- [`00acb20c`](#insn-00acb20c) → [`00a466f8`](../00a46/00a466f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a466f8` · 推定シンボル `None` · 推定型 `None`
- [`00acb214`](#insn-00acb214) → [`00acb270`](#insn-00acb270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb21c`](#insn-00acb21c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb228`](#insn-00acb228) → `00337d90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb24c`](#insn-00acb24c) → [`00a469c0`](../00a46/00a469c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a469c0` · 推定シンボル `None` · 推定型 `None`
- [`00acb254`](#insn-00acb254) → [`008b6e60`](../008b6/008b6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6e60` · 推定シンボル `None` · 推定型 `None`
- [`00acb25c`](#insn-00acb25c) → [`00a466f8`](../00a46/00a466f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a466f8` · 推定シンボル `None` · 推定型 `None`
- [`00acb264`](#insn-00acb264) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb268`](#insn-00acb268) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb26c`](#insn-00acb26c) → [`00a466e0`](../00a46/00a466e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a466e0` · 推定シンボル `None` · 推定型 `None`
- [`00acb274`](#insn-00acb274) → [`00a466e0`](../00a46/00a466e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a466e0` · 推定シンボル `None` · 推定型 `None`
- [`00acb27c`](#insn-00acb27c) → [`00acb2b0`](#insn-00acb2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb284`](#insn-00acb284) → [`00acb298`](#insn-00acb298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb288`](#insn-00acb288) → [`00acb2d8`](#insn-00acb2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb28c`](#insn-00acb28c) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00acb294`](#insn-00acb294) → [`00acb2a0`](#insn-00acb2a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb298`](#insn-00acb298) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00acb2a4`](#insn-00acb2a4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2a8`](#insn-00acb2a8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2ac`](#insn-00acb2ac) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00acb2b0`](#insn-00acb2b0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb2bc`](#insn-00acb2bc) → `00337e60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acb2c0`](#insn-00acb2c0) → [`00acb2e4`](#insn-00acb2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2cc`](#insn-00acb2cc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2d0`](#insn-00acb2d0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2d8`](#insn-00acb2d8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2dc`](#insn-00acb2dc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2e4`](#insn-00acb2e4) → [`00459d34`](../00459/00459d34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459d34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acb1ec`](#insn-00acb1ec)

~~~json
{
  "source": "00acb1ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1f0`](#insn-00acb1f0)

~~~json
{
  "source": "00acb1f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb204`](#insn-00acb204)

~~~json
{
  "source": "00acb204",
  "target": "008b6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb20c`](#insn-00acb20c)

~~~json
{
  "source": "00acb20c",
  "target": "00a466f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb214`](#insn-00acb214)

~~~json
{
  "source": "00acb214",
  "target": "00acb270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb21c`](#insn-00acb21c)

~~~json
{
  "source": "00acb21c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb228`](#insn-00acb228)

~~~json
{
  "source": "00acb228",
  "target": "00337d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337d90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "60a37d00b0660a00",
  "capture_start": "00337d90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb24c`](#insn-00acb24c)

~~~json
{
  "source": "00acb24c",
  "target": "00a469c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb254`](#insn-00acb254)

~~~json
{
  "source": "00acb254",
  "target": "008b6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb25c`](#insn-00acb25c)

~~~json
{
  "source": "00acb25c",
  "target": "00a466f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb264`](#insn-00acb264)

~~~json
{
  "source": "00acb264",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb268`](#insn-00acb268)

~~~json
{
  "source": "00acb268",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb26c`](#insn-00acb26c)

~~~json
{
  "source": "00acb26c",
  "target": "00a466e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb274`](#insn-00acb274)

~~~json
{
  "source": "00acb274",
  "target": "00a466e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb27c`](#insn-00acb27c)

~~~json
{
  "source": "00acb27c",
  "target": "00acb2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb284`](#insn-00acb284)

~~~json
{
  "source": "00acb284",
  "target": "00acb298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb288`](#insn-00acb288)

~~~json
{
  "source": "00acb288",
  "target": "00acb2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb28c`](#insn-00acb28c)

~~~json
{
  "source": "00acb28c",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb294`](#insn-00acb294)

~~~json
{
  "source": "00acb294",
  "target": "00acb2a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb298`](#insn-00acb298)

~~~json
{
  "source": "00acb298",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2a4`](#insn-00acb2a4)

~~~json
{
  "source": "00acb2a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2a8`](#insn-00acb2a8)

~~~json
{
  "source": "00acb2a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2ac`](#insn-00acb2ac)

~~~json
{
  "source": "00acb2ac",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2b0`](#insn-00acb2b0)

~~~json
{
  "source": "00acb2b0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2bc`](#insn-00acb2bc)

~~~json
{
  "source": "00acb2bc",
  "target": "00337e60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337e60",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "70a97d0060690a00",
  "capture_start": "00337e60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acb2c0`](#insn-00acb2c0)

~~~json
{
  "source": "00acb2c0",
  "target": "00acb2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2cc`](#insn-00acb2cc)

~~~json
{
  "source": "00acb2cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2d0`](#insn-00acb2d0)

~~~json
{
  "source": "00acb2d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2d8`](#insn-00acb2d8)

~~~json
{
  "source": "00acb2d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2dc`](#insn-00acb2dc)

~~~json
{
  "source": "00acb2dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2e4`](#insn-00acb2e4)

~~~json
{
  "source": "00acb2e4",
  "target": "00459d34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
