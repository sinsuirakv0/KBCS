# 00acbd2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acad38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acad38.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-5e2641c6965f6173d4d8a3cc8a8f09ba)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbd2c",
  "name": "FUN_00acbd2c",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be207e4e7c2dee98c7044792ac07b38c173a6cb844ef96892887081ebd43a4b9",
  "source_text_sha256": "be207e4e7c2dee98c7044792ac07b38c173a6cb844ef96892887081ebd43a4b9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbd2c",
        "00acbe0f"
      ]
    ],
    "bytes_sha256": "0119b0c652fddf5923e6c0d602ece73c281e0ab2eb095a71e5aeae87462dd192",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [006af7a4](../006af/006af7a4.md)
- [00831ea0](../00831/00831ea0.md)

## 呼び出し先

- [0057c208](../0057c/0057c208.md)
- [00aca5f8](../00aca/00aca5f8.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acbd2c(long param_1,long *param_2)

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
  FUN_0057c208(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acbde0;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acbde0:
  FUN_00aca5f8(param_1);
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
<a id="insn-00acbd2c"></a> `00acbd2c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbd30"></a> `00acbd30` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbd34"></a> `00acbd34` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbd38"></a> `00acbd38` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbd3c"></a> `00acbd3c` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acbd40"></a> `00acbd40` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbd44"></a> `00acbd44` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbd48"></a> `00acbd48` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acbd4c"></a> `00acbd4c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbd50"></a> `00acbd50` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acbd54"></a> `00acbd54` | `20 10 40 f9` | ldr x0,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd58"></a> `00acbd58` | `68 82 02 39` | strb w8,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00acbd5c"></a> `00acbd5c` | `7f a6 00 b9` | str wzr,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00acbd60"></a> `00acbd60` | `00 01 00 b4` | cbz x0,0x00acbd80 | `CONDITIONAL_JUMP`
<a id="insn-00acbd64"></a> `00acbd64` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00acbd68"></a> `00acbd68` | `00 01 00 54` | b.eq 0x00acbd88 | `CONDITIONAL_JUMP`
<a id="insn-00acbd6c"></a> `00acbd6c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbd70"></a> `00acbd70` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbd74"></a> `00acbd74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbd78"></a> `00acbd78` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd7c"></a> `00acbd7c` | `0a 00 00 14` | b 0x00acbda4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd80"></a> `00acbd80` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd84"></a> `00acbd84` | `08 00 00 14` | b 0x00acbda4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd88"></a> `00acbd88` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acbd8c"></a> `00acbd8c` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00acbd90"></a> `00acbd90` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00acbd94"></a> `00acbd94` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd98"></a> `00acbd98` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acbd9c"></a> `00acbd9c` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00acbda0"></a> `00acbda0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbda4"></a> `00acbda4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acbda8"></a> `00acbda8` | `61 02 05 91` | add x1,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00acbdac"></a> `00acbdac` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00acbdb0"></a> `00acbdb0` | `16 c1 ea 97` | bl 0x0057c208 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdb4"></a> `00acbdb4` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbdb8"></a> `00acbdb8` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00acbdbc"></a> `00acbdbc` | `80 00 00 54` | b.eq 0x00acbdcc | `CONDITIONAL_JUMP`
<a id="insn-00acbdc0"></a> `00acbdc0` | `00 01 00 b4` | cbz x0,0x00acbde0 | `CONDITIONAL_JUMP`
<a id="insn-00acbdc4"></a> `00acbdc4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acbdc8"></a> `00acbdc8` | `03 00 00 14` | b 0x00acbdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbdcc"></a> `00acbdcc` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acbdd0"></a> `00acbdd0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acbdd4"></a> `00acbdd4` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acbdd8"></a> `00acbdd8` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acbddc"></a> `00acbddc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbde0"></a> `00acbde0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbde4"></a> `00acbde4` | `05 fa ff 97` | bl 0x00aca5f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acbde8"></a> `00acbde8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acbdec"></a> `00acbdec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbdf0"></a> `00acbdf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbdf4"></a> `00acbdf4` | `c1 00 00 54` | b.ne 0x00acbe0c | `CONDITIONAL_JUMP`
<a id="insn-00acbdf8"></a> `00acbdf8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbdfc"></a> `00acbdfc` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbe00"></a> `00acbe00` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbe04"></a> `00acbe04` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbe08"></a> `00acbe08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbe0c"></a> `00acbe0c` | `5d 34 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbd2c`](#insn-00acbd2c) 範囲 `[['00acbd2c', '00acbd63']]`
  - `CONDITIONAL_JUMP` [`00acbd60`](#insn-00acbd60) → [`00acbd80`](#insn-00acbd80)
  - `FALL_THROUGH` [`00acbd60`](#insn-00acbd60) → [`00acbd64`](#insn-00acbd64)
- ブロック [`00acbd64`](#insn-00acbd64) 範囲 `[['00acbd64', '00acbd6b']]`
  - `CONDITIONAL_JUMP` [`00acbd68`](#insn-00acbd68) → [`00acbd88`](#insn-00acbd88)
  - `FALL_THROUGH` [`00acbd68`](#insn-00acbd68) → [`00acbd6c`](#insn-00acbd6c)
- ブロック [`00acbd6c`](#insn-00acbd6c) 範囲 `[['00acbd6c', '00acbd7f']]`
  - `UNCONDITIONAL_JUMP` [`00acbd7c`](#insn-00acbd7c) → [`00acbda4`](#insn-00acbda4)
- ブロック [`00acbd80`](#insn-00acbd80) 範囲 `[['00acbd80', '00acbd87']]`
  - `UNCONDITIONAL_JUMP` [`00acbd84`](#insn-00acbd84) → [`00acbda4`](#insn-00acbda4)
- ブロック [`00acbd88`](#insn-00acbd88) 範囲 `[['00acbd88', '00acbda3']]`
  - `FALL_THROUGH` [`00acbda0`](#insn-00acbda0) → [`00acbda4`](#insn-00acbda4)
- ブロック [`00acbda4`](#insn-00acbda4) 範囲 `[['00acbda4', '00acbdbf']]`
  - `CONDITIONAL_JUMP` [`00acbdbc`](#insn-00acbdbc) → [`00acbdcc`](#insn-00acbdcc)
  - `FALL_THROUGH` [`00acbdbc`](#insn-00acbdbc) → [`00acbdc0`](#insn-00acbdc0)
- ブロック [`00acbdc0`](#insn-00acbdc0) 範囲 `[['00acbdc0', '00acbdc3']]`
  - `CONDITIONAL_JUMP` [`00acbdc0`](#insn-00acbdc0) → [`00acbde0`](#insn-00acbde0)
  - `FALL_THROUGH` [`00acbdc0`](#insn-00acbdc0) → [`00acbdc4`](#insn-00acbdc4)
- ブロック [`00acbdc4`](#insn-00acbdc4) 範囲 `[['00acbdc4', '00acbdcb']]`
  - `UNCONDITIONAL_JUMP` [`00acbdc8`](#insn-00acbdc8) → [`00acbdd4`](#insn-00acbdd4)
- ブロック [`00acbdcc`](#insn-00acbdcc) 範囲 `[['00acbdcc', '00acbdd3']]`
  - `FALL_THROUGH` [`00acbdd0`](#insn-00acbdd0) → [`00acbdd4`](#insn-00acbdd4)
- ブロック [`00acbdd4`](#insn-00acbdd4) 範囲 `[['00acbdd4', '00acbddf']]`
  - `FALL_THROUGH` [`00acbddc`](#insn-00acbddc) → [`00acbde0`](#insn-00acbde0)
- ブロック [`00acbde0`](#insn-00acbde0) 範囲 `[['00acbde0', '00acbdf7']]`
  - `CONDITIONAL_JUMP` [`00acbdf4`](#insn-00acbdf4) → [`00acbe0c`](#insn-00acbe0c)
  - `FALL_THROUGH` [`00acbdf4`](#insn-00acbdf4) → [`00acbdf8`](#insn-00acbdf8)
- ブロック [`00acbdf8`](#insn-00acbdf8) 範囲 `[['00acbdf8', '00acbe0b']]`
- ブロック [`00acbe0c`](#insn-00acbe0c) 範囲 `[['00acbe0c', '00acbe0f']]`

## 命令位置別の参照

- [`00acbd30`](#insn-00acbd30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd34`](#insn-00acbd34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd38`](#insn-00acbd38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd4c`](#insn-00acbd4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd60`](#insn-00acbd60) → [`00acbd80`](#insn-00acbd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd68`](#insn-00acbd68) → [`00acbd88`](#insn-00acbd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd78`](#insn-00acbd78) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd7c`](#insn-00acbd7c) → [`00acbda4`](#insn-00acbda4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd80`](#insn-00acbd80) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd84`](#insn-00acbd84) → [`00acbda4`](#insn-00acbda4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd94`](#insn-00acbd94) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdb0`](#insn-00acbdb0) → [`0057c208`](../0057c/0057c208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057c208` · 推定シンボル `None` · 推定型 `None`
- [`00acbdb4`](#insn-00acbdb4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdbc`](#insn-00acbdbc) → [`00acbdcc`](#insn-00acbdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc0`](#insn-00acbdc0) → [`00acbde0`](#insn-00acbde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc8`](#insn-00acbdc8) → [`00acbdd4`](#insn-00acbdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdd4`](#insn-00acbdd4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbde4`](#insn-00acbde4) → [`00aca5f8`](../00aca/00aca5f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aca5f8` · 推定シンボル `None` · 推定型 `None`
- [`00acbdec`](#insn-00acbdec) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf4`](#insn-00acbdf4) → [`00acbe0c`](#insn-00acbe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf8`](#insn-00acbdf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdfc`](#insn-00acbdfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe00`](#insn-00acbe00) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe0c`](#insn-00acbe0c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbd30`](#insn-00acbd30)

~~~json
{
  "source": "00acbd30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd34`](#insn-00acbd34)

~~~json
{
  "source": "00acbd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd38`](#insn-00acbd38)

~~~json
{
  "source": "00acbd38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd4c`](#insn-00acbd4c)

~~~json
{
  "source": "00acbd4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd60`](#insn-00acbd60)

~~~json
{
  "source": "00acbd60",
  "target": "00acbd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd68`](#insn-00acbd68)

~~~json
{
  "source": "00acbd68",
  "target": "00acbd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd78`](#insn-00acbd78)

~~~json
{
  "source": "00acbd78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd7c`](#insn-00acbd7c)

~~~json
{
  "source": "00acbd7c",
  "target": "00acbda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd80`](#insn-00acbd80)

~~~json
{
  "source": "00acbd80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd84`](#insn-00acbd84)

~~~json
{
  "source": "00acbd84",
  "target": "00acbda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd94`](#insn-00acbd94)

~~~json
{
  "source": "00acbd94",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdb0`](#insn-00acbdb0)

~~~json
{
  "source": "00acbdb0",
  "target": "0057c208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdb4`](#insn-00acbdb4)

~~~json
{
  "source": "00acbdb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdbc`](#insn-00acbdbc)

~~~json
{
  "source": "00acbdbc",
  "target": "00acbdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc0`](#insn-00acbdc0)

~~~json
{
  "source": "00acbdc0",
  "target": "00acbde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc8`](#insn-00acbdc8)

~~~json
{
  "source": "00acbdc8",
  "target": "00acbdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdd4`](#insn-00acbdd4)

~~~json
{
  "source": "00acbdd4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbde4`](#insn-00acbde4)

~~~json
{
  "source": "00acbde4",
  "target": "00aca5f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdec`](#insn-00acbdec)

~~~json
{
  "source": "00acbdec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf4`](#insn-00acbdf4)

~~~json
{
  "source": "00acbdf4",
  "target": "00acbe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf8`](#insn-00acbdf8)

~~~json
{
  "source": "00acbdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdfc`](#insn-00acbdfc)

~~~json
{
  "source": "00acbdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe00`](#insn-00acbe00)

~~~json
{
  "source": "00acbe00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe0c`](#insn-00acbe0c)

~~~json
{
  "source": "00acbe0c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
