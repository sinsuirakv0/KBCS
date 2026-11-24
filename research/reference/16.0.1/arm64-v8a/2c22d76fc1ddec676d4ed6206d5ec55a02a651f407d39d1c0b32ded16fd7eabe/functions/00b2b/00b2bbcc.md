# 00b2bbcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2b7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-387d9c5267477bc66d5039aca8d08a23)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b2bc68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bc68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-d14324d9d9d8ea65f9eb49a9c0b601b6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2bbcc",
  "name": "FUN_00b2bbcc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d",
  "source_text_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2bbcc",
        "00b2bc2f"
      ]
    ],
    "bytes_sha256": "7231fb51bbd11e1f62ac324ba99624973fc5fc1f0bbc94a9ecb35896be73d45b",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0043b5a8](../0043b/0043b5a8.md)
- [0043b658](../0043b/0043b658.md)

## 呼び出し先

- [0046caa4](../0046c/0046caa4.md)
- [0046cabc](../0046c/0046cabc.md)
- [0046cac8](../0046c/0046cac8.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00b2bbcc(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_008514f8();
  if ((param_2 & 1) == 0) {
    FUN_0046caa4(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_0046cabc();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_008514f8();
      FUN_0046cac8(uVar2,0);
    }
    uVar2 = FUN_008514f8();
    FUN_0046caa4(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_008514f8();
                    /* WARNING: Could not recover jumptable at 0x00b2bc2c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2bbcc"></a> `00b2bbcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b2bbd0"></a> `00b2bbd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bbd4"></a> `00b2bbd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b2bbd8"></a> `00b2bbd8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00b2bbdc"></a> `00b2bbdc` | `47 96 f4 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bbe0"></a> `00b2bbe0` | `73 01 00 36` | tbz w19,#0x0,0x00b2bc0c | `CONDITIONAL_JUMP`
<a id="insn-00b2bbe4"></a> `00b2bbe4` | `b6 03 e5 97` | bl 0x0046cabc | `UNCONDITIONAL_CALL`
<a id="insn-00b2bbe8"></a> `00b2bbe8` | `80 00 00 36` | tbz w0,#0x0,0x00b2bbf8 | `CONDITIONAL_JUMP`
<a id="insn-00b2bbec"></a> `00b2bbec` | `43 96 f4 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bbf0"></a> `00b2bbf0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b2bbf4"></a> `00b2bbf4` | `b5 03 e5 97` | bl 0x0046cac8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bbf8"></a> `00b2bbf8` | `40 96 f4 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bbfc"></a> `00b2bbfc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b2bc00"></a> `00b2bc00` | `a9 03 e5 97` | bl 0x0046caa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bc04"></a> `00b2bc04` | `13 02 80 52` | mov w19,#0x10 | `FALL_THROUGH`
<a id="insn-00b2bc08"></a> `00b2bc08` | `04 00 00 14` | b 0x00b2bc18 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2bc0c"></a> `00b2bc0c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b2bc10"></a> `00b2bc10` | `a5 03 e5 97` | bl 0x0046caa4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bc14"></a> `00b2bc14` | `13 03 80 52` | mov w19,#0x18 | `FALL_THROUGH`
<a id="insn-00b2bc18"></a> `00b2bc18` | `38 96 f4 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bc1c"></a> `00b2bc1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b2bc20"></a> `00b2bc20` | `01 69 73 f8` | ldr x1,[x8, x19, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b2bc24"></a> `00b2bc24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bc28"></a> `00b2bc28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b2bc2c"></a> `00b2bc2c` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b2bbcc`](#insn-00b2bbcc) 範囲 `[['00b2bbcc', '00b2bbe3']]`
  - `CONDITIONAL_JUMP` [`00b2bbe0`](#insn-00b2bbe0) → [`00b2bc0c`](#insn-00b2bc0c)
  - `FALL_THROUGH` [`00b2bbe0`](#insn-00b2bbe0) → [`00b2bbe4`](#insn-00b2bbe4)
- ブロック [`00b2bbe4`](#insn-00b2bbe4) 範囲 `[['00b2bbe4', '00b2bbeb']]`
  - `CONDITIONAL_JUMP` [`00b2bbe8`](#insn-00b2bbe8) → [`00b2bbf8`](#insn-00b2bbf8)
  - `FALL_THROUGH` [`00b2bbe8`](#insn-00b2bbe8) → [`00b2bbec`](#insn-00b2bbec)
- ブロック [`00b2bbec`](#insn-00b2bbec) 範囲 `[['00b2bbec', '00b2bbf7']]`
  - `FALL_THROUGH` [`00b2bbf4`](#insn-00b2bbf4) → [`00b2bbf8`](#insn-00b2bbf8)
- ブロック [`00b2bbf8`](#insn-00b2bbf8) 範囲 `[['00b2bbf8', '00b2bc0b']]`
  - `UNCONDITIONAL_JUMP` [`00b2bc08`](#insn-00b2bc08) → [`00b2bc18`](#insn-00b2bc18)
- ブロック [`00b2bc0c`](#insn-00b2bc0c) 範囲 `[['00b2bc0c', '00b2bc17']]`
  - `FALL_THROUGH` [`00b2bc14`](#insn-00b2bc14) → [`00b2bc18`](#insn-00b2bc18)
- ブロック [`00b2bc18`](#insn-00b2bc18) 範囲 `[['00b2bc18', '00b2bc2f']]`

## 命令位置別の参照

- [`00b2bbcc`](#insn-00b2bbcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbd0`](#insn-00b2bbd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbdc`](#insn-00b2bbdc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbe0`](#insn-00b2bbe0) → [`00b2bc0c`](#insn-00b2bc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbe4`](#insn-00b2bbe4) → [`0046cabc`](../0046c/0046cabc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cabc` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbe8`](#insn-00b2bbe8) → [`00b2bbf8`](#insn-00b2bbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbec`](#insn-00b2bbec) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbf4`](#insn-00b2bbf4) → [`0046cac8`](../0046c/0046cac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cac8` · 推定シンボル `None` · 推定型 `None`
- [`00b2bbf8`](#insn-00b2bbf8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc00`](#insn-00b2bc00) → [`0046caa4`](../0046c/0046caa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046caa4` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc08`](#insn-00b2bc08) → [`00b2bc18`](#insn-00b2bc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc10`](#insn-00b2bc10) → [`0046caa4`](../0046c/0046caa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046caa4` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc18`](#insn-00b2bc18) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc24`](#insn-00b2bc24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bc28`](#insn-00b2bc28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2bbcc`](#insn-00b2bbcc)

~~~json
{
  "source": "00b2bbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bbd0`](#insn-00b2bbd0)

~~~json
{
  "source": "00b2bbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bbdc`](#insn-00b2bbdc)

~~~json
{
  "source": "00b2bbdc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bbe0`](#insn-00b2bbe0)

~~~json
{
  "source": "00b2bbe0",
  "target": "00b2bc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bbe4`](#insn-00b2bbe4)

~~~json
{
  "source": "00b2bbe4",
  "target": "0046cabc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bbe8`](#insn-00b2bbe8)

~~~json
{
  "source": "00b2bbe8",
  "target": "00b2bbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bbec`](#insn-00b2bbec)

~~~json
{
  "source": "00b2bbec",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bbf4`](#insn-00b2bbf4)

~~~json
{
  "source": "00b2bbf4",
  "target": "0046cac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bbf8`](#insn-00b2bbf8)

~~~json
{
  "source": "00b2bbf8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bc00`](#insn-00b2bc00)

~~~json
{
  "source": "00b2bc00",
  "target": "0046caa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bc08`](#insn-00b2bc08)

~~~json
{
  "source": "00b2bc08",
  "target": "00b2bc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bc10`](#insn-00b2bc10)

~~~json
{
  "source": "00b2bc10",
  "target": "0046caa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bc18`](#insn-00b2bc18)

~~~json
{
  "source": "00b2bc18",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bc24`](#insn-00b2bc24)

~~~json
{
  "source": "00b2bc24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bc28`](#insn-00b2bc28)

~~~json
{
  "source": "00b2bc28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
