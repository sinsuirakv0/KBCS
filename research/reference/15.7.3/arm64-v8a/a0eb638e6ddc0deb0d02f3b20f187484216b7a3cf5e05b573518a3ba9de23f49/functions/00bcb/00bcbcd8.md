# 00bcbcd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcbc10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbc10.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-5dbe212a0d1be6c5c8454a1dd1b9389e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcbd1c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-a5e156ded9141c1f83c8b558cb59839c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbcd8",
  "name": "FUN_00bcbcd8",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcecb67ba08165b05dafece96ea45d1654731b3594bcedb5ceb088e35879e033",
  "source_text_sha256": "dcecb67ba08165b05dafece96ea45d1654731b3594bcedb5ceb088e35879e033",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbcd8",
        "00bcbdf7"
      ]
    ],
    "bytes_sha256": "5018efc33364a439e8d3ba27c3084277fffd47cae9aac527e822bfe883df87ce",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 関連文字列（未確認候補）

~~~text
" requires "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1958 bytes

~~~c

void FUN_00bcbcd8(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  undefined8 uVar3;
  void *__ptr;
  long lVar4;
  size_t __size;
  long *plVar5;
  
  plVar5 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar5 + 0x20))(plVar5);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  if (*(long *)(param_1 + 0x28) != 0) {
    lVar4 = param_2[1];
    __ptr = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 10U) {
      __size = param_2[2] * 2;
      uVar1 = lVar4 + 0x3ea;
      if (__size < uVar1 || __size - uVar1 == 0) {
        __size = uVar1;
      }
      param_2[2] = __size;
      __ptr = realloc(__ptr,__size);
                    /* try { // try from 00bcbd60 to 00ccbdc3 has its CatchHandler @ 00bcbd60
                       catch() { ... } // from try @ 00bcbd60 with catch @ 00bcbd60
                       catch() { ... } // from try @ 00bcbdd4 with catch @ 00bcbd60 */
      *param_2 = __ptr;
      if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    uVar3 = s_requires_002af880._0_8_;
    pcVar2 = (char *)((long)__ptr + lVar4);
    pcVar2[8] = 's';
    pcVar2[9] = ' ';
    *(undefined8 *)pcVar2 = uVar3;
    plVar5 = *(long **)(param_1 + 0x28);
    lVar4 = *plVar5;
    param_2[1] = param_2[1] + 10;
    (**(code **)(lVar4 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bcbdd4 to 00ccbecb has its CatchHandler @ 00bcbd60 */
                    /* WARNING: Could not recover jumptable at 0x00bcbdf0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
      return;
    }
  }
                    /* try { // try from 00bcbdc4 to 00ccbdd3 has its CatchHandler @ 00bcbe8c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbcd8"></a> `00bcbcd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbcdc"></a> `00bcbcdc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbce0"></a> `00bcbce0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbce4"></a> `00bcbce4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbce8"></a> `00bcbce8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbcec"></a> `00bcbcec` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbcf0"></a> `00bcbcf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbcf4"></a> `00bcbcf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbcf8"></a> `00bcbcf8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbcfc"></a> `00bcbcfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbd00"></a> `00bcbd00` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbd04"></a> `00bcbd04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbd08"></a> `00bcbd08` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbd0c"></a> `00bcbd0c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbd10"></a> `00bcbd10` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbd14"></a> `00bcbd14` | `c0 00 00 54` | b.eq 0x00bcbd2c | `CONDITIONAL_JUMP`
<a id="insn-00bcbd18"></a> `00bcbd18` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbd1c"></a> `00bcbd1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbd20"></a> `00bcbd20` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbd24"></a> `00bcbd24` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbd28"></a> `00bcbd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbd2c"></a> `00bcbd2c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbd30"></a> `00bcbd30` | `68 04 00 b4` | cbz x8,0x00bcbdbc | `CONDITIONAL_JUMP`
<a id="insn-00bcbd34"></a> `00bcbd34` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbd38"></a> `00bcbd38` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbd3c"></a> `00bcbd3c` | `0a 29 00 91` | add x10,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcbd40"></a> `00bcbd40` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbd44"></a> `00bcbd44` | `49 01 00 54` | b.ls 0x00bcbd6c | `CONDITIONAL_JUMP`
<a id="insn-00bcbd48"></a> `00bcbd48` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbd4c"></a> `00bcbd4c` | `08 a9 0f 91` | add x8,x8,#0x3ea | `FALL_THROUGH`
<a id="insn-00bcbd50"></a> `00bcbd50` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbd54"></a> `00bcbd54` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbd58"></a> `00bcbd58` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd5c"></a> `00bcbd5c` | `29 45 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbd60"></a> `00bcbd60` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbd64"></a> `00bcbd64` | `80 04 00 b4` | cbz x0,0x00bcbdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbd68"></a> `00bcbd68` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbd6c"></a> `00bcbd6c` | `29 b7 ff 90` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00bcbd70"></a> `00bcbd70` | `29 01 22 91` | add x9,x9,#0x880 | `FALL_THROUGH`
<a id="insn-00bcbd74"></a> `00bcbd74` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbd78"></a> `00bcbd78` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbd7c"></a> `00bcbd7c` | `6a 0e 84 52` | mov w10,#0x2073 | `FALL_THROUGH`
<a id="insn-00bcbd80"></a> `00bcbd80` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbd84"></a> `00bcbd84` | `0a 11 00 79` | strh w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbd88"></a> `00bcbd88` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbd8c"></a> `00bcbd8c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbd90"></a> `00bcbd90` | `94 16 40 f9` | ldr x20,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbd94"></a> `00bcbd94` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcbd98"></a> `00bcbd98` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcbd9c"></a> `00bcbd9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbda0"></a> `00bcbda0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbda4"></a> `00bcbda4` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbda8"></a> `00bcbda8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbdac"></a> `00bcbdac` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbdb0"></a> `00bcbdb0` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbdb4"></a> `00bcbdb4` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbdb8"></a> `00bcbdb8` | `c1 00 00 54` | b.ne 0x00bcbdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbdbc"></a> `00bcbdbc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbdc0"></a> `00bcbdc0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdc4"></a> `00bcbdc4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbdc8"></a> `00bcbdc8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbdcc"></a> `00bcbdcc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbdd0"></a> `00bcbdd0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbdd4"></a> `00bcbdd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbdd8"></a> `00bcbdd8` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbddc"></a> `00bcbddc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbde0"></a> `00bcbde0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbde4"></a> `00bcbde4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbde8"></a> `00bcbde8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbdec"></a> `00bcbdec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `1f 49 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbcd8`](#insn-00bcbcd8) 範囲 `[['00bcbcd8', '00bcbd17']]`
  - `CONDITIONAL_JUMP` [`00bcbd14`](#insn-00bcbd14) → [`00bcbd2c`](#insn-00bcbd2c)
  - `FALL_THROUGH` [`00bcbd14`](#insn-00bcbd14) → [`00bcbd18`](#insn-00bcbd18)
- ブロック [`00bcbd18`](#insn-00bcbd18) 範囲 `[['00bcbd18', '00bcbd2b']]`
  - `FALL_THROUGH` [`00bcbd28`](#insn-00bcbd28) → [`00bcbd2c`](#insn-00bcbd2c)
- ブロック [`00bcbd2c`](#insn-00bcbd2c) 範囲 `[['00bcbd2c', '00bcbd33']]`
  - `CONDITIONAL_JUMP` [`00bcbd30`](#insn-00bcbd30) → [`00bcbdbc`](#insn-00bcbdbc)
  - `FALL_THROUGH` [`00bcbd30`](#insn-00bcbd30) → [`00bcbd34`](#insn-00bcbd34)
- ブロック [`00bcbd34`](#insn-00bcbd34) 範囲 `[['00bcbd34', '00bcbd47']]`
  - `CONDITIONAL_JUMP` [`00bcbd44`](#insn-00bcbd44) → [`00bcbd6c`](#insn-00bcbd6c)
  - `FALL_THROUGH` [`00bcbd44`](#insn-00bcbd44) → [`00bcbd48`](#insn-00bcbd48)
- ブロック [`00bcbd48`](#insn-00bcbd48) 範囲 `[['00bcbd48', '00bcbd5f']]`
  - `FALL_THROUGH` [`00bcbd5c`](#insn-00bcbd5c) → [`00bcbd60`](#insn-00bcbd60)
- ブロック [`00bcbd60`](#insn-00bcbd60) 範囲 `[['00bcbd60', '00bcbd67']]`
  - `CONDITIONAL_JUMP` [`00bcbd64`](#insn-00bcbd64) → [`00bcbdf4`](#insn-00bcbdf4)
  - `FALL_THROUGH` [`00bcbd64`](#insn-00bcbd64) → [`00bcbd68`](#insn-00bcbd68)
- ブロック [`00bcbd68`](#insn-00bcbd68) 範囲 `[['00bcbd68', '00bcbd6b']]`
  - `FALL_THROUGH` [`00bcbd68`](#insn-00bcbd68) → [`00bcbd6c`](#insn-00bcbd6c)
- ブロック [`00bcbd6c`](#insn-00bcbd6c) 範囲 `[['00bcbd6c', '00bcbdbb']]`
  - `CONDITIONAL_JUMP` [`00bcbdb8`](#insn-00bcbdb8) → [`00bcbdd0`](#insn-00bcbdd0)
  - `FALL_THROUGH` [`00bcbdb8`](#insn-00bcbdb8) → [`00bcbdbc`](#insn-00bcbdbc)
- ブロック [`00bcbdbc`](#insn-00bcbdbc) 範囲 `[['00bcbdbc', '00bcbdc3']]`
  - `FALL_THROUGH` [`00bcbdc0`](#insn-00bcbdc0) → [`00bcbdc4`](#insn-00bcbdc4)
- ブロック [`00bcbdc4`](#insn-00bcbdc4) 範囲 `[['00bcbdc4', '00bcbdcf']]`
- ブロック [`00bcbdd0`](#insn-00bcbdd0) 範囲 `[['00bcbdd0', '00bcbdd3']]`
  - `FALL_THROUGH` [`00bcbdd0`](#insn-00bcbdd0) → [`00bcbdd4`](#insn-00bcbdd4)
- ブロック [`00bcbdd4`](#insn-00bcbdd4) 範囲 `[['00bcbdd4', '00bcbdf3']]`
- ブロック [`00bcbdf4`](#insn-00bcbdf4) 範囲 `[['00bcbdf4', '00bcbdf7']]`

## 命令位置別の参照

- [`00bcbcdc`](#insn-00bcbcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce0`](#insn-00bcbce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce4`](#insn-00bcbce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd14`](#insn-00bcbd14) → [`00bcbd2c`](#insn-00bcbd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd30`](#insn-00bcbd30) → [`00bcbdbc`](#insn-00bcbdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd44`](#insn-00bcbd44) → [`00bcbd6c`](#insn-00bcbd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd5c`](#insn-00bcbd5c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd64`](#insn-00bcbd64) → [`00bcbdf4`](#insn-00bcbdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd78`](#insn-00bcbd78) → `002af880`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbdb8`](#insn-00bcbdb8) → [`00bcbdd0`](#insn-00bcbdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdbc`](#insn-00bcbdbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdc0`](#insn-00bcbdc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdc4`](#insn-00bcbdc4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde0`](#insn-00bcbde0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde4`](#insn-00bcbde4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde8`](#insn-00bcbde8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf4`](#insn-00bcbdf4) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbcdc`](#insn-00bcbcdc)

~~~json
{
  "source": "00bcbcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbce0`](#insn-00bcbce0)

~~~json
{
  "source": "00bcbce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbce4`](#insn-00bcbce4)

~~~json
{
  "source": "00bcbce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd14`](#insn-00bcbd14)

~~~json
{
  "source": "00bcbd14",
  "target": "00bcbd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd30`](#insn-00bcbd30)

~~~json
{
  "source": "00bcbd30",
  "target": "00bcbdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd44`](#insn-00bcbd44)

~~~json
{
  "source": "00bcbd44",
  "target": "00bcbd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd5c`](#insn-00bcbd5c)

~~~json
{
  "source": "00bcbd5c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd64`](#insn-00bcbd64)

~~~json
{
  "source": "00bcbd64",
  "target": "00bcbdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd78`](#insn-00bcbd78)

~~~json
{
  "source": "00bcbd78",
  "target": "002af880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af880",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "2072657175697265732000",
  "capture_start": "002af880",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbdb8`](#insn-00bcbdb8)

~~~json
{
  "source": "00bcbdb8",
  "target": "00bcbdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdbc`](#insn-00bcbdbc)

~~~json
{
  "source": "00bcbdbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdc0`](#insn-00bcbdc0)

~~~json
{
  "source": "00bcbdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdc4`](#insn-00bcbdc4)

~~~json
{
  "source": "00bcbdc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbde0`](#insn-00bcbde0)

~~~json
{
  "source": "00bcbde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbde4`](#insn-00bcbde4)

~~~json
{
  "source": "00bcbde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbde8`](#insn-00bcbde8)

~~~json
{
  "source": "00bcbde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdf4`](#insn-00bcbdf4)

~~~json
{
  "source": "00bcbdf4",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
