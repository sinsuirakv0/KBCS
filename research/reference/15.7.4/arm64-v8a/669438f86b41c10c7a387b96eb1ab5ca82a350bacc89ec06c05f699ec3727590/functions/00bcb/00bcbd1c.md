# 00bcbd1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcbcd8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-a5e156ded9141c1f83c8b558cb59839c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c48764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-463541c92b5186430cbbbaffb53c64c8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbd1c",
  "name": "FUN_00bcbd1c",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9feb5539b588aeaba3e2c4abf8769ce3f82102aea7dadc1d938aa03e8b23d76",
  "source_text_sha256": "f9feb5539b588aeaba3e2c4abf8769ce3f82102aea7dadc1d938aa03e8b23d76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbd1c",
        "00bcbe3b"
      ]
    ],
    "bytes_sha256": "8d5ad816e4abd6cd3a279a2d46e816ed9e7014397854ecca5b4a967d90681ff3",
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

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
" requires "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1958 bytes

~~~c

void FUN_00bcbd1c(long param_1,undefined8 *param_2)

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
                    /* try { // try from 00bcbda4 to 00ccbe07 has its CatchHandler @ 00bcbda4
                       catch() { ... } // from try @ 00bcbda4 with catch @ 00bcbda4
                       catch() { ... } // from try @ 00bcbe18 with catch @ 00bcbda4 */
      *param_2 = __ptr;
      if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    uVar3 = s_requires_002af7ec._0_8_;
    pcVar2 = (char *)((long)__ptr + lVar4);
    pcVar2[8] = 's';
    pcVar2[9] = ' ';
    *(undefined8 *)pcVar2 = uVar3;
    plVar5 = *(long **)(param_1 + 0x28);
    lVar4 = *plVar5;
    param_2[1] = param_2[1] + 10;
    (**(code **)(lVar4 + 0x20))(plVar5,param_2);
    if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
                    /* try { // try from 00bcbe18 to 00ccbf0f has its CatchHandler @ 00bcbda4 */
                    /* WARNING: Could not recover jumptable at 0x00bcbe34. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
      return;
    }
  }
                    /* try { // try from 00bcbe08 to 00ccbe17 has its CatchHandler @ 00bcbed0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbd1c"></a> `00bcbd1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbd20"></a> `00bcbd20` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbd24"></a> `00bcbd24` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd28"></a> `00bcbd28` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbd2c"></a> `00bcbd2c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbd30"></a> `00bcbd30` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd34"></a> `00bcbd34` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbd38"></a> `00bcbd38` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbd3c"></a> `00bcbd3c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbd40"></a> `00bcbd40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbd44"></a> `00bcbd44` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbd48"></a> `00bcbd48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbd4c"></a> `00bcbd4c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbd50"></a> `00bcbd50` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbd54"></a> `00bcbd54` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbd58"></a> `00bcbd58` | `c0 00 00 54` | b.eq 0x00bcbd70 | `CONDITIONAL_JUMP`
<a id="insn-00bcbd5c"></a> `00bcbd5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcbd60"></a> `00bcbd60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcbd64"></a> `00bcbd64` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbd68"></a> `00bcbd68` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbd6c"></a> `00bcbd6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbd70"></a> `00bcbd70` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbd74"></a> `00bcbd74` | `68 04 00 b4` | cbz x8,0x00bcbe00 | `CONDITIONAL_JUMP`
<a id="insn-00bcbd78"></a> `00bcbd78` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbd7c"></a> `00bcbd7c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbd80"></a> `00bcbd80` | `0a 29 00 91` | add x10,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcbd84"></a> `00bcbd84` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbd88"></a> `00bcbd88` | `49 01 00 54` | b.ls 0x00bcbdb0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbd8c"></a> `00bcbd8c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbd90"></a> `00bcbd90` | `08 a9 0f 91` | add x8,x8,#0x3ea | `FALL_THROUGH`
<a id="insn-00bcbd94"></a> `00bcbd94` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbd98"></a> `00bcbd98` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbd9c"></a> `00bcbd9c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbda0"></a> `00bcbda0` | `2c 45 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbda4"></a> `00bcbda4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbda8"></a> `00bcbda8` | `80 04 00 b4` | cbz x0,0x00bcbe38 | `CONDITIONAL_JUMP`
<a id="insn-00bcbdac"></a> `00bcbdac` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbdb0"></a> `00bcbdb0` | `29 b7 ff 90` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00bcbdb4"></a> `00bcbdb4` | `29 b1 1f 91` | add x9,x9,#0x7ec | `FALL_THROUGH`
<a id="insn-00bcbdb8"></a> `00bcbdb8` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbdbc"></a> `00bcbdbc` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbdc0"></a> `00bcbdc0` | `6a 0e 84 52` | mov w10,#0x2073 | `FALL_THROUGH`
<a id="insn-00bcbdc4"></a> `00bcbdc4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbdc8"></a> `00bcbdc8` | `0a 11 00 79` | strh w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbdcc"></a> `00bcbdcc` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbdd0"></a> `00bcbdd0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbdd4"></a> `00bcbdd4` | `94 16 40 f9` | ldr x20,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbdd8"></a> `00bcbdd8` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcbddc"></a> `00bcbddc` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcbde0"></a> `00bcbde0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbde4"></a> `00bcbde4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbde8"></a> `00bcbde8` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbdec"></a> `00bcbdec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbdf8"></a> `00bcbdf8` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbdfc"></a> `00bcbdfc` | `c1 00 00 54` | b.ne 0x00bcbe14 | `CONDITIONAL_JUMP`
<a id="insn-00bcbe00"></a> `00bcbe00` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbe04"></a> `00bcbe04` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe08"></a> `00bcbe08` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbe0c"></a> `00bcbe0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbe10"></a> `00bcbe10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbe14"></a> `00bcbe14` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbe18"></a> `00bcbe18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbe1c"></a> `00bcbe1c` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbe20"></a> `00bcbe20` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbe24"></a> `00bcbe24` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbe28"></a> `00bcbe28` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe2c"></a> `00bcbe2c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbe30"></a> `00bcbe30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbe34"></a> `00bcbe34` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcbe38"></a> `00bcbe38` | `22 49 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbd1c`](#insn-00bcbd1c) 範囲 `[['00bcbd1c', '00bcbd5b']]`
  - `CONDITIONAL_JUMP` [`00bcbd58`](#insn-00bcbd58) → [`00bcbd70`](#insn-00bcbd70)
  - `FALL_THROUGH` [`00bcbd58`](#insn-00bcbd58) → [`00bcbd5c`](#insn-00bcbd5c)
- ブロック [`00bcbd5c`](#insn-00bcbd5c) 範囲 `[['00bcbd5c', '00bcbd6f']]`
  - `FALL_THROUGH` [`00bcbd6c`](#insn-00bcbd6c) → [`00bcbd70`](#insn-00bcbd70)
- ブロック [`00bcbd70`](#insn-00bcbd70) 範囲 `[['00bcbd70', '00bcbd77']]`
  - `CONDITIONAL_JUMP` [`00bcbd74`](#insn-00bcbd74) → [`00bcbe00`](#insn-00bcbe00)
  - `FALL_THROUGH` [`00bcbd74`](#insn-00bcbd74) → [`00bcbd78`](#insn-00bcbd78)
- ブロック [`00bcbd78`](#insn-00bcbd78) 範囲 `[['00bcbd78', '00bcbd8b']]`
  - `CONDITIONAL_JUMP` [`00bcbd88`](#insn-00bcbd88) → [`00bcbdb0`](#insn-00bcbdb0)
  - `FALL_THROUGH` [`00bcbd88`](#insn-00bcbd88) → [`00bcbd8c`](#insn-00bcbd8c)
- ブロック [`00bcbd8c`](#insn-00bcbd8c) 範囲 `[['00bcbd8c', '00bcbda3']]`
  - `FALL_THROUGH` [`00bcbda0`](#insn-00bcbda0) → [`00bcbda4`](#insn-00bcbda4)
- ブロック [`00bcbda4`](#insn-00bcbda4) 範囲 `[['00bcbda4', '00bcbdab']]`
  - `CONDITIONAL_JUMP` [`00bcbda8`](#insn-00bcbda8) → [`00bcbe38`](#insn-00bcbe38)
  - `FALL_THROUGH` [`00bcbda8`](#insn-00bcbda8) → [`00bcbdac`](#insn-00bcbdac)
- ブロック [`00bcbdac`](#insn-00bcbdac) 範囲 `[['00bcbdac', '00bcbdaf']]`
  - `FALL_THROUGH` [`00bcbdac`](#insn-00bcbdac) → [`00bcbdb0`](#insn-00bcbdb0)
- ブロック [`00bcbdb0`](#insn-00bcbdb0) 範囲 `[['00bcbdb0', '00bcbdff']]`
  - `CONDITIONAL_JUMP` [`00bcbdfc`](#insn-00bcbdfc) → [`00bcbe14`](#insn-00bcbe14)
  - `FALL_THROUGH` [`00bcbdfc`](#insn-00bcbdfc) → [`00bcbe00`](#insn-00bcbe00)
- ブロック [`00bcbe00`](#insn-00bcbe00) 範囲 `[['00bcbe00', '00bcbe07']]`
  - `FALL_THROUGH` [`00bcbe04`](#insn-00bcbe04) → [`00bcbe08`](#insn-00bcbe08)
- ブロック [`00bcbe08`](#insn-00bcbe08) 範囲 `[['00bcbe08', '00bcbe13']]`
- ブロック [`00bcbe14`](#insn-00bcbe14) 範囲 `[['00bcbe14', '00bcbe17']]`
  - `FALL_THROUGH` [`00bcbe14`](#insn-00bcbe14) → [`00bcbe18`](#insn-00bcbe18)
- ブロック [`00bcbe18`](#insn-00bcbe18) 範囲 `[['00bcbe18', '00bcbe37']]`
- ブロック [`00bcbe38`](#insn-00bcbe38) 範囲 `[['00bcbe38', '00bcbe3b']]`

## 命令位置別の参照

- [`00bcbd20`](#insn-00bcbd20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd24`](#insn-00bcbd24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd28`](#insn-00bcbd28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd58`](#insn-00bcbd58) → [`00bcbd70`](#insn-00bcbd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd74`](#insn-00bcbd74) → [`00bcbe00`](#insn-00bcbe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd88`](#insn-00bcbd88) → [`00bcbdb0`](#insn-00bcbdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbda0`](#insn-00bcbda0) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcbda8`](#insn-00bcbda8) → [`00bcbe38`](#insn-00bcbe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdbc`](#insn-00bcbdbc) → `002af7ec`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbdfc`](#insn-00bcbdfc) → [`00bcbe14`](#insn-00bcbe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe00`](#insn-00bcbe00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe04`](#insn-00bcbe04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe08`](#insn-00bcbe08) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe24`](#insn-00bcbe24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe28`](#insn-00bcbe28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe2c`](#insn-00bcbe2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe38`](#insn-00bcbe38) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbd20`](#insn-00bcbd20)

~~~json
{
  "source": "00bcbd20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd24`](#insn-00bcbd24)

~~~json
{
  "source": "00bcbd24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd28`](#insn-00bcbd28)

~~~json
{
  "source": "00bcbd28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd58`](#insn-00bcbd58)

~~~json
{
  "source": "00bcbd58",
  "target": "00bcbd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd74`](#insn-00bcbd74)

~~~json
{
  "source": "00bcbd74",
  "target": "00bcbe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd88`](#insn-00bcbd88)

~~~json
{
  "source": "00bcbd88",
  "target": "00bcbdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbda0`](#insn-00bcbda0)

~~~json
{
  "source": "00bcbda0",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbda8`](#insn-00bcbda8)

~~~json
{
  "source": "00bcbda8",
  "target": "00bcbe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdbc`](#insn-00bcbdbc)

~~~json
{
  "source": "00bcbdbc",
  "target": "002af7ec",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af7ec",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "2072657175697265732000",
  "capture_start": "002af7ec",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbdfc`](#insn-00bcbdfc)

~~~json
{
  "source": "00bcbdfc",
  "target": "00bcbe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe00`](#insn-00bcbe00)

~~~json
{
  "source": "00bcbe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe04`](#insn-00bcbe04)

~~~json
{
  "source": "00bcbe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe08`](#insn-00bcbe08)

~~~json
{
  "source": "00bcbe08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe24`](#insn-00bcbe24)

~~~json
{
  "source": "00bcbe24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe28`](#insn-00bcbe28)

~~~json
{
  "source": "00bcbe28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe2c`](#insn-00bcbe2c)

~~~json
{
  "source": "00bcbe2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe38`](#insn-00bcbe38)

~~~json
{
  "source": "00bcbe38",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
