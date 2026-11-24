# 00afaf2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9f38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9f38.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-58f61ac5f34a486420fbda0487e342cd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaf2c",
  "name": "FUN_00afaf2c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ddc1c6436a6cfe8bc5893c1ffac608add1ffc79793564d76aa912b004fcb3368",
  "source_text_sha256": "ddc1c6436a6cfe8bc5893c1ffac608add1ffc79793564d76aa912b004fcb3368",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaf2c",
        "00afaf9b"
      ]
    ],
    "bytes_sha256": "11748a56925eb2f388ae66ab0fbd507463c8a9e0acecd0dfc25a674e6f304ea6",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00afaf2c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008524fc();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaf2c"></a> `00afaf2c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afaf30"></a> `00afaf30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf34"></a> `00afaf34` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaf38"></a> `00afaf38` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaf3c"></a> `00afaf3c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaf40"></a> `00afaf40` | `6f 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaf44"></a> `00afaf44` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afaf48"></a> `00afaf48` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afaf4c"></a> `00afaf4c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaf50"></a> `00afaf50` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afaf54"></a> `00afaf54` | `2f b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf58"></a> `00afaf58` | `60 00 00 37` | tbnz w0,#0x0,0x00afaf64 | `CONDITIONAL_JUMP`
<a id="insn-00afaf5c"></a> `00afaf5c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afaf60"></a> `00afaf60` | `0c 00 00 14` | b 0x00afaf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaf64"></a> `00afaf64` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afaf68"></a> `00afaf68` | `65 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaf6c"></a> `00afaf6c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaf70"></a> `00afaf70` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaf74"></a> `00afaf74` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaf78"></a> `00afaf78` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaf7c"></a> `00afaf7c` | `89 7b 89 52` | mov w9,#0x4bdc | `FALL_THROUGH`
<a id="insn-00afaf80"></a> `00afaf80` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaf84"></a> `00afaf84` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaf88"></a> `00afaf88` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afaf8c"></a> `00afaf8c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afaf90"></a> `00afaf90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf94"></a> `00afaf94` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afaf98"></a> `00afaf98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaf2c`](#insn-00afaf2c) 範囲 `[['00afaf2c', '00afaf5b']]`
  - `CONDITIONAL_JUMP` [`00afaf58`](#insn-00afaf58) → [`00afaf64`](#insn-00afaf64)
  - `FALL_THROUGH` [`00afaf58`](#insn-00afaf58) → [`00afaf5c`](#insn-00afaf5c)
- ブロック [`00afaf5c`](#insn-00afaf5c) 範囲 `[['00afaf5c', '00afaf63']]`
  - `UNCONDITIONAL_JUMP` [`00afaf60`](#insn-00afaf60) → [`00afaf90`](#insn-00afaf90)
- ブロック [`00afaf64`](#insn-00afaf64) 範囲 `[['00afaf64', '00afaf8f']]`
  - `FALL_THROUGH` [`00afaf8c`](#insn-00afaf8c) → [`00afaf90`](#insn-00afaf90)
- ブロック [`00afaf90`](#insn-00afaf90) 範囲 `[['00afaf90', '00afaf9b']]`

## 命令位置別の参照

- [`00afaf2c`](#insn-00afaf2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf30`](#insn-00afaf30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf40`](#insn-00afaf40) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaf54`](#insn-00afaf54) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afaf58`](#insn-00afaf58) → [`00afaf64`](#insn-00afaf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf60`](#insn-00afaf60) → [`00afaf90`](#insn-00afaf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf68`](#insn-00afaf68) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaf90`](#insn-00afaf90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf94`](#insn-00afaf94) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaf2c`](#insn-00afaf2c)

~~~json
{
  "source": "00afaf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf30`](#insn-00afaf30)

~~~json
{
  "source": "00afaf30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf40`](#insn-00afaf40)

~~~json
{
  "source": "00afaf40",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf54`](#insn-00afaf54)

~~~json
{
  "source": "00afaf54",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf58`](#insn-00afaf58)

~~~json
{
  "source": "00afaf58",
  "target": "00afaf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf60`](#insn-00afaf60)

~~~json
{
  "source": "00afaf60",
  "target": "00afaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf68`](#insn-00afaf68)

~~~json
{
  "source": "00afaf68",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf90`](#insn-00afaf90)

~~~json
{
  "source": "00afaf90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf94`](#insn-00afaf94)

~~~json
{
  "source": "00afaf94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
