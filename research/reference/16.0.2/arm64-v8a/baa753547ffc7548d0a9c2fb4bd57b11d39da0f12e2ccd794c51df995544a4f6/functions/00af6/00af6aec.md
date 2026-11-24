# 00af6aec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af6a50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6a50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0035.md#compare-47b894e14a54cea6f6e0dcbbbc85874b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af7ae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af7ae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-347048977f39d0dcdaab7493a2fe4f6a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af6aec",
  "name": "FUN_00af6aec",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce7c961229cfa9648a679c0ccd23a0a41a369ffc01b622d5e3567257f9167bc1",
  "source_text_sha256": "ce7c961229cfa9648a679c0ccd23a0a41a369ffc01b622d5e3567257f9167bc1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af6aec",
        "00af6b5b"
      ]
    ],
    "bytes_sha256": "cc1bfb557f4408923af4fa427756b48c862b90571445a204be927651eb4d91c2",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00af6aec(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_00851550();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a7c) != 0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af6aec"></a> `00af6aec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af6af0"></a> `00af6af0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6af4"></a> `00af6af4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af6af8"></a> `00af6af8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af6afc"></a> `00af6afc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af6b00"></a> `00af6b00` | `94 6a f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af6b04"></a> `00af6b04` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af6b08"></a> `00af6b08` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af6b0c"></a> `00af6b0c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af6b10"></a> `00af6b10` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af6b14"></a> `00af6b14` | `53 c2 eb 97` | bl 0x005e7460 | `UNCONDITIONAL_CALL`
<a id="insn-00af6b18"></a> `00af6b18` | `a0 01 00 37` | tbnz w0,#0x0,0x00af6b4c | `CONDITIONAL_JUMP`
<a id="insn-00af6b1c"></a> `00af6b1c` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af6b20"></a> `00af6b20` | `8c 6a f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af6b24"></a> `00af6b24` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af6b28"></a> `00af6b28` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af6b2c"></a> `00af6b2c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af6b30"></a> `00af6b30` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af6b34"></a> `00af6b34` | `89 4f 89 52` | mov w9,#0x4a7c | `FALL_THROUGH`
<a id="insn-00af6b38"></a> `00af6b38` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af6b3c"></a> `00af6b3c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af6b40"></a> `00af6b40` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af6b44"></a> `00af6b44` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00af6b48"></a> `00af6b48` | `02 00 00 14` | b 0x00af6b50 | `UNCONDITIONAL_JUMP`
<a id="insn-00af6b4c"></a> `00af6b4c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00af6b50"></a> `00af6b50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6b54"></a> `00af6b54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6b58"></a> `00af6b58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af6aec`](#insn-00af6aec) 範囲 `[['00af6aec', '00af6b1b']]`
  - `CONDITIONAL_JUMP` [`00af6b18`](#insn-00af6b18) → [`00af6b4c`](#insn-00af6b4c)
  - `FALL_THROUGH` [`00af6b18`](#insn-00af6b18) → [`00af6b1c`](#insn-00af6b1c)
- ブロック [`00af6b1c`](#insn-00af6b1c) 範囲 `[['00af6b1c', '00af6b4b']]`
  - `UNCONDITIONAL_JUMP` [`00af6b48`](#insn-00af6b48) → [`00af6b50`](#insn-00af6b50)
- ブロック [`00af6b4c`](#insn-00af6b4c) 範囲 `[['00af6b4c', '00af6b4f']]`
  - `FALL_THROUGH` [`00af6b4c`](#insn-00af6b4c) → [`00af6b50`](#insn-00af6b50)
- ブロック [`00af6b50`](#insn-00af6b50) 範囲 `[['00af6b50', '00af6b5b']]`

## 命令位置別の参照

- [`00af6aec`](#insn-00af6aec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6af0`](#insn-00af6af0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6b00`](#insn-00af6b00) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af6b14`](#insn-00af6b14) → [`005e7460`](../005e7/005e7460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7460` · 推定シンボル `None` · 推定型 `None`
- [`00af6b18`](#insn-00af6b18) → [`00af6b4c`](#insn-00af6b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6b20`](#insn-00af6b20) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af6b48`](#insn-00af6b48) → [`00af6b50`](#insn-00af6b50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6b50`](#insn-00af6b50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6b54`](#insn-00af6b54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af6aec`](#insn-00af6aec)

~~~json
{
  "source": "00af6aec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6af0`](#insn-00af6af0)

~~~json
{
  "source": "00af6af0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6b00`](#insn-00af6b00)

~~~json
{
  "source": "00af6b00",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6b14`](#insn-00af6b14)

~~~json
{
  "source": "00af6b14",
  "target": "005e7460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6b18`](#insn-00af6b18)

~~~json
{
  "source": "00af6b18",
  "target": "00af6b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6b20`](#insn-00af6b20)

~~~json
{
  "source": "00af6b20",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6b48`](#insn-00af6b48)

~~~json
{
  "source": "00af6b48",
  "target": "00af6b50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6b50`](#insn-00af6b50)

~~~json
{
  "source": "00af6b50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6b54`](#insn-00af6b54)

~~~json
{
  "source": "00af6b54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
