# 00acacc8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acaacc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaacc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-59bee5bd326d340a38aa6e5d6609e46a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acad38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acad38.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-97bd3c6ea02536d5c9d144b30c6985b1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acacc8",
  "name": "FUN_00acacc8",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee35d251443d76ee4cdfb00a0a9e061025745981e4d8b8c08e07a320dfb8c1ef",
  "source_text_sha256": "ee35d251443d76ee4cdfb00a0a9e061025745981e4d8b8c08e07a320dfb8c1ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acacc8",
        "00acadab"
      ]
    ],
    "bytes_sha256": "2e31d61e8d83d0312e9aafac4b0a6069ee0f9afd3b1246341f568482c428bbdb",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [006af39c](../006af/006af39c.md)
- [00830e9c](../00830/00830e9c.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [00ac9594](../00ac9/00ac9594.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acacc8(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)param_2[4];
  *(undefined1 *)(param_1 + 0xa0) = 1;
  *(undefined4 *)(param_1 + 0xa4) = 0;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_2) {
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057bea8(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acad7c;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acad7c:
  FUN_00ac9594(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acacc8"></a> `00acacc8` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acaccc"></a> `00acaccc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acacd0"></a> `00acacd0` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acacd4"></a> `00acacd4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acacd8"></a> `00acacd8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acacdc"></a> `00acacdc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acace0"></a> `00acace0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acace4"></a> `00acace4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acace8"></a> `00acace8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acacec"></a> `00acacec` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acacf0"></a> `00acacf0` | `20 10 40 f9` | ldr x0,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acacf4"></a> `00acacf4` | `68 82 02 39` | strb w8,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00acacf8"></a> `00acacf8` | `7f a6 00 b9` | str wzr,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00acacfc"></a> `00acacfc` | `00 01 00 b4` | cbz x0,0x00acad1c | `CONDITIONAL_JUMP`
<a id="insn-00acad00"></a> `00acad00` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00acad04"></a> `00acad04` | `00 01 00 54` | b.eq 0x00acad24 | `CONDITIONAL_JUMP`
<a id="insn-00acad08"></a> `00acad08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acad0c"></a> `00acad0c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acad10"></a> `00acad10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acad14"></a> `00acad14` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acad18"></a> `00acad18` | `0a 00 00 14` | b 0x00acad40 | `UNCONDITIONAL_JUMP`
<a id="insn-00acad1c"></a> `00acad1c` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acad20"></a> `00acad20` | `08 00 00 14` | b 0x00acad40 | `UNCONDITIONAL_JUMP`
<a id="insn-00acad24"></a> `00acad24` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acad28"></a> `00acad28` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00acad2c"></a> `00acad2c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00acad30"></a> `00acad30` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acad34"></a> `00acad34` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acad38"></a> `00acad38` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00acad3c"></a> `00acad3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acad40"></a> `00acad40` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acad44"></a> `00acad44` | `61 02 05 91` | add x1,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00acad48"></a> `00acad48` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00acad4c"></a> `00acad4c` | `57 c4 ea 97` | bl 0x0057bea8 | `UNCONDITIONAL_CALL`
<a id="insn-00acad50"></a> `00acad50` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acad54"></a> `00acad54` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00acad58"></a> `00acad58` | `80 00 00 54` | b.eq 0x00acad68 | `CONDITIONAL_JUMP`
<a id="insn-00acad5c"></a> `00acad5c` | `00 01 00 b4` | cbz x0,0x00acad7c | `CONDITIONAL_JUMP`
<a id="insn-00acad60"></a> `00acad60` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acad64"></a> `00acad64` | `03 00 00 14` | b 0x00acad70 | `UNCONDITIONAL_JUMP`
<a id="insn-00acad68"></a> `00acad68` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acad6c"></a> `00acad6c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acad70"></a> `00acad70` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acad74"></a> `00acad74` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acad78"></a> `00acad78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acad7c"></a> `00acad7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acad80"></a> `00acad80` | `05 fa ff 97` | bl 0x00ac9594 | `UNCONDITIONAL_CALL`
<a id="insn-00acad84"></a> `00acad84` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acad88"></a> `00acad88` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acad8c"></a> `00acad8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acad90"></a> `00acad90` | `c1 00 00 54` | b.ne 0x00acada8 | `CONDITIONAL_JUMP`
<a id="insn-00acad94"></a> `00acad94` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acad98"></a> `00acad98` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acad9c"></a> `00acad9c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acada0"></a> `00acada0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acada4"></a> `00acada4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acada8"></a> `00acada8` | `4e 34 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acacc8`](#insn-00acacc8) 範囲 `[['00acacc8', '00acacff']]`
  - `CONDITIONAL_JUMP` [`00acacfc`](#insn-00acacfc) → [`00acad1c`](#insn-00acad1c)
  - `FALL_THROUGH` [`00acacfc`](#insn-00acacfc) → [`00acad00`](#insn-00acad00)
- ブロック [`00acad00`](#insn-00acad00) 範囲 `[['00acad00', '00acad07']]`
  - `CONDITIONAL_JUMP` [`00acad04`](#insn-00acad04) → [`00acad24`](#insn-00acad24)
  - `FALL_THROUGH` [`00acad04`](#insn-00acad04) → [`00acad08`](#insn-00acad08)
- ブロック [`00acad08`](#insn-00acad08) 範囲 `[['00acad08', '00acad1b']]`
  - `UNCONDITIONAL_JUMP` [`00acad18`](#insn-00acad18) → [`00acad40`](#insn-00acad40)
- ブロック [`00acad1c`](#insn-00acad1c) 範囲 `[['00acad1c', '00acad23']]`
  - `UNCONDITIONAL_JUMP` [`00acad20`](#insn-00acad20) → [`00acad40`](#insn-00acad40)
- ブロック [`00acad24`](#insn-00acad24) 範囲 `[['00acad24', '00acad3f']]`
  - `FALL_THROUGH` [`00acad3c`](#insn-00acad3c) → [`00acad40`](#insn-00acad40)
- ブロック [`00acad40`](#insn-00acad40) 範囲 `[['00acad40', '00acad5b']]`
  - `CONDITIONAL_JUMP` [`00acad58`](#insn-00acad58) → [`00acad68`](#insn-00acad68)
  - `FALL_THROUGH` [`00acad58`](#insn-00acad58) → [`00acad5c`](#insn-00acad5c)
- ブロック [`00acad5c`](#insn-00acad5c) 範囲 `[['00acad5c', '00acad5f']]`
  - `CONDITIONAL_JUMP` [`00acad5c`](#insn-00acad5c) → [`00acad7c`](#insn-00acad7c)
  - `FALL_THROUGH` [`00acad5c`](#insn-00acad5c) → [`00acad60`](#insn-00acad60)
- ブロック [`00acad60`](#insn-00acad60) 範囲 `[['00acad60', '00acad67']]`
  - `UNCONDITIONAL_JUMP` [`00acad64`](#insn-00acad64) → [`00acad70`](#insn-00acad70)
- ブロック [`00acad68`](#insn-00acad68) 範囲 `[['00acad68', '00acad6f']]`
  - `FALL_THROUGH` [`00acad6c`](#insn-00acad6c) → [`00acad70`](#insn-00acad70)
- ブロック [`00acad70`](#insn-00acad70) 範囲 `[['00acad70', '00acad7b']]`
  - `FALL_THROUGH` [`00acad78`](#insn-00acad78) → [`00acad7c`](#insn-00acad7c)
- ブロック [`00acad7c`](#insn-00acad7c) 範囲 `[['00acad7c', '00acad93']]`
  - `CONDITIONAL_JUMP` [`00acad90`](#insn-00acad90) → [`00acada8`](#insn-00acada8)
  - `FALL_THROUGH` [`00acad90`](#insn-00acad90) → [`00acad94`](#insn-00acad94)
- ブロック [`00acad94`](#insn-00acad94) 範囲 `[['00acad94', '00acada7']]`
- ブロック [`00acada8`](#insn-00acada8) 範囲 `[['00acada8', '00acadab']]`

## 命令位置別の参照

- [`00acaccc`](#insn-00acaccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacd0`](#insn-00acacd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacd4`](#insn-00acacd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acace8`](#insn-00acace8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacfc`](#insn-00acacfc) → [`00acad1c`](#insn-00acad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad04`](#insn-00acad04) → [`00acad24`](#insn-00acad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad14`](#insn-00acad14) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad18`](#insn-00acad18) → [`00acad40`](#insn-00acad40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad1c`](#insn-00acad1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad20`](#insn-00acad20) → [`00acad40`](#insn-00acad40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad30`](#insn-00acad30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad4c`](#insn-00acad4c) → [`0057bea8`](../0057b/0057bea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057bea8` · 推定シンボル `None` · 推定型 `None`
- [`00acad50`](#insn-00acad50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad58`](#insn-00acad58) → [`00acad68`](#insn-00acad68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad5c`](#insn-00acad5c) → [`00acad7c`](#insn-00acad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad64`](#insn-00acad64) → [`00acad70`](#insn-00acad70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad70`](#insn-00acad70) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad80`](#insn-00acad80) → [`00ac9594`](../00ac9/00ac9594.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9594` · 推定シンボル `None` · 推定型 `None`
- [`00acad88`](#insn-00acad88) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad90`](#insn-00acad90) → [`00acada8`](#insn-00acada8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad94`](#insn-00acad94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad98`](#insn-00acad98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad9c`](#insn-00acad9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acada8`](#insn-00acada8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaccc`](#insn-00acaccc)

~~~json
{
  "source": "00acaccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacd0`](#insn-00acacd0)

~~~json
{
  "source": "00acacd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacd4`](#insn-00acacd4)

~~~json
{
  "source": "00acacd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acace8`](#insn-00acace8)

~~~json
{
  "source": "00acace8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacfc`](#insn-00acacfc)

~~~json
{
  "source": "00acacfc",
  "target": "00acad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad04`](#insn-00acad04)

~~~json
{
  "source": "00acad04",
  "target": "00acad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad14`](#insn-00acad14)

~~~json
{
  "source": "00acad14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad18`](#insn-00acad18)

~~~json
{
  "source": "00acad18",
  "target": "00acad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad1c`](#insn-00acad1c)

~~~json
{
  "source": "00acad1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad20`](#insn-00acad20)

~~~json
{
  "source": "00acad20",
  "target": "00acad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad30`](#insn-00acad30)

~~~json
{
  "source": "00acad30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad4c`](#insn-00acad4c)

~~~json
{
  "source": "00acad4c",
  "target": "0057bea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad50`](#insn-00acad50)

~~~json
{
  "source": "00acad50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad58`](#insn-00acad58)

~~~json
{
  "source": "00acad58",
  "target": "00acad68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad5c`](#insn-00acad5c)

~~~json
{
  "source": "00acad5c",
  "target": "00acad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad64`](#insn-00acad64)

~~~json
{
  "source": "00acad64",
  "target": "00acad70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad70`](#insn-00acad70)

~~~json
{
  "source": "00acad70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad80`](#insn-00acad80)

~~~json
{
  "source": "00acad80",
  "target": "00ac9594",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad88`](#insn-00acad88)

~~~json
{
  "source": "00acad88",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad90`](#insn-00acad90)

~~~json
{
  "source": "00acad90",
  "target": "00acada8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad94`](#insn-00acad94)

~~~json
{
  "source": "00acad94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad98`](#insn-00acad98)

~~~json
{
  "source": "00acad98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad9c`](#insn-00acad9c)

~~~json
{
  "source": "00acad9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acada8`](#insn-00acada8)

~~~json
{
  "source": "00acada8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
