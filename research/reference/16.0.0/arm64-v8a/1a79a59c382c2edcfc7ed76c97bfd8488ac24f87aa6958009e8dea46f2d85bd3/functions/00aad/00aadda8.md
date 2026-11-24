# 00aadda8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a4fd84`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd84.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-7c545081ee04569b400d23fa6acb01af)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aadfa4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadfa4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-1cec938081c31b28cf9606191e9f66a7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadda8",
  "name": "FUN_00aadda8",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33a86f8414a1dc6ddd9eb117f430b9555ce8055b9cb8945ae9d1706464bdb9a7",
  "source_text_sha256": "33a86f8414a1dc6ddd9eb117f430b9555ce8055b9cb8945ae9d1706464bdb9a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadda8",
        "00aade23"
      ]
    ],
    "bytes_sha256": "1a9c85fccbd04788745ad3f6da2fd4991575042288b31ff6b7d0b5347b5936cf",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 542 bytes

~~~c

void FUN_00aadda8(long param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  
  pbVar2 = *(byte **)(param_1 + 8);
  if (pbVar2 == (byte *)0x0) {
    return;
  }
  pbVar1 = *(byte **)(param_1 + 0x10);
  pbVar3 = pbVar2;
  if (pbVar1 != pbVar2) {
    do {
      pbVar3 = pbVar1 + -0x18;
      if ((*pbVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar1 + -8));
      }
      pbVar1 = pbVar3;
    } while (pbVar3 != pbVar2);
    pbVar3 = *(byte **)(param_1 + 8);
  }
  *(byte **)(param_1 + 0x10) = pbVar2;
  _ZdlPv(pbVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadda8"></a> `00aadda8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aaddac"></a> `00aaddac` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaddb0"></a> `00aaddb0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaddb4"></a> `00aaddb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaddb8"></a> `00aaddb8` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aaddbc"></a> `00aaddbc` | `d4 02 00 b4` | cbz x20,0x00aade14 | `CONDITIONAL_JUMP`
<a id="insn-00aaddc0"></a> `00aaddc0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaddc4"></a> `00aaddc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaddc8"></a> `00aaddc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaddcc"></a> `00aaddcc` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00aaddd0"></a> `00aaddd0` | `80 01 00 54` | b.eq 0x00aade00 | `CONDITIONAL_JUMP`
<a id="insn-00aaddd4"></a> `00aaddd4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00aaddd8"></a> `00aaddd8` | `04 00 00 14` | b 0x00aadde8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadddc"></a> `00aadddc` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00aadde0"></a> `00aadde0` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00aadde4"></a> `00aadde4` | `c0 00 00 54` | b.eq 0x00aaddfc | `CONDITIONAL_JUMP`
<a id="insn-00aadde8"></a> `00aadde8` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00aaddec"></a> `00aaddec` | `89 ff 07 36` | tbz w9,#0x0,0x00aadddc | `CONDITIONAL_JUMP`
<a id="insn-00aaddf0"></a> `00aaddf0` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaddf4"></a> `00aaddf4` | `2f a7 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaddf8"></a> `00aaddf8` | `f9 ff ff 17` | b 0x00aadddc | `UNCONDITIONAL_JUMP`
<a id="insn-00aaddfc"></a> `00aaddfc` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aade00"></a> `00aade00` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aade04"></a> `00aade04` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aade08"></a> `00aade08` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aade0c"></a> `00aade0c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aade10"></a> `00aade10` | `28 a7 06 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00aade14"></a> `00aade14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aade18"></a> `00aade18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aade1c"></a> `00aade1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aade20"></a> `00aade20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadda8`](#insn-00aadda8) 範囲 `[['00aadda8', '00aaddbf']]`
  - `CONDITIONAL_JUMP` [`00aaddbc`](#insn-00aaddbc) → [`00aade14`](#insn-00aade14)
  - `FALL_THROUGH` [`00aaddbc`](#insn-00aaddbc) → [`00aaddc0`](#insn-00aaddc0)
- ブロック [`00aaddc0`](#insn-00aaddc0) 範囲 `[['00aaddc0', '00aaddd3']]`
  - `CONDITIONAL_JUMP` [`00aaddd0`](#insn-00aaddd0) → [`00aade00`](#insn-00aade00)
  - `FALL_THROUGH` [`00aaddd0`](#insn-00aaddd0) → [`00aaddd4`](#insn-00aaddd4)
- ブロック [`00aaddd4`](#insn-00aaddd4) 範囲 `[['00aaddd4', '00aadddb']]`
  - `UNCONDITIONAL_JUMP` [`00aaddd8`](#insn-00aaddd8) → [`00aadde8`](#insn-00aadde8)
- ブロック [`00aadddc`](#insn-00aadddc) 範囲 `[['00aadddc', '00aadde7']]`
  - `CONDITIONAL_JUMP` [`00aadde4`](#insn-00aadde4) → [`00aaddfc`](#insn-00aaddfc)
  - `FALL_THROUGH` [`00aadde4`](#insn-00aadde4) → [`00aadde8`](#insn-00aadde8)
- ブロック [`00aadde8`](#insn-00aadde8) 範囲 `[['00aadde8', '00aaddef']]`
  - `CONDITIONAL_JUMP` [`00aaddec`](#insn-00aaddec) → [`00aadddc`](#insn-00aadddc)
  - `FALL_THROUGH` [`00aaddec`](#insn-00aaddec) → [`00aaddf0`](#insn-00aaddf0)
- ブロック [`00aaddf0`](#insn-00aaddf0) 範囲 `[['00aaddf0', '00aaddfb']]`
  - `UNCONDITIONAL_JUMP` [`00aaddf8`](#insn-00aaddf8) → [`00aadddc`](#insn-00aadddc)
- ブロック [`00aaddfc`](#insn-00aaddfc) 範囲 `[['00aaddfc', '00aaddff']]`
  - `FALL_THROUGH` [`00aaddfc`](#insn-00aaddfc) → [`00aade00`](#insn-00aade00)
- ブロック [`00aade00`](#insn-00aade00) 範囲 `[['00aade00', '00aade13']]`
- ブロック [`00aade14`](#insn-00aade14) 範囲 `[['00aade14', '00aade23']]`

## 命令位置別の参照

- [`00aadda8`](#insn-00aadda8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddac`](#insn-00aaddac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb0`](#insn-00aaddb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddbc`](#insn-00aaddbc) → [`00aade14`](#insn-00aade14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd0`](#insn-00aaddd0) → [`00aade00`](#insn-00aade00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd8`](#insn-00aaddd8) → [`00aadde8`](#insn-00aadde8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadde4`](#insn-00aadde4) → [`00aaddfc`](#insn-00aaddfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddec`](#insn-00aaddec) → [`00aadddc`](#insn-00aadddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf4`](#insn-00aaddf4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf8`](#insn-00aaddf8) → [`00aadddc`](#insn-00aadddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade04`](#insn-00aade04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade08`](#insn-00aade08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade0c`](#insn-00aade0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade10`](#insn-00aade10) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aade14`](#insn-00aade14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade18`](#insn-00aade18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade1c`](#insn-00aade1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadda8`](#insn-00aadda8)

~~~json
{
  "source": "00aadda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddac`](#insn-00aaddac)

~~~json
{
  "source": "00aaddac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb0`](#insn-00aaddb0)

~~~json
{
  "source": "00aaddb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddbc`](#insn-00aaddbc)

~~~json
{
  "source": "00aaddbc",
  "target": "00aade14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddd0`](#insn-00aaddd0)

~~~json
{
  "source": "00aaddd0",
  "target": "00aade00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddd8`](#insn-00aaddd8)

~~~json
{
  "source": "00aaddd8",
  "target": "00aadde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadde4`](#insn-00aadde4)

~~~json
{
  "source": "00aadde4",
  "target": "00aaddfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddec`](#insn-00aaddec)

~~~json
{
  "source": "00aaddec",
  "target": "00aadddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf4`](#insn-00aaddf4)

~~~json
{
  "source": "00aaddf4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaddf8`](#insn-00aaddf8)

~~~json
{
  "source": "00aaddf8",
  "target": "00aadddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade04`](#insn-00aade04)

~~~json
{
  "source": "00aade04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade08`](#insn-00aade08)

~~~json
{
  "source": "00aade08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade0c`](#insn-00aade0c)

~~~json
{
  "source": "00aade0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade10`](#insn-00aade10)

~~~json
{
  "source": "00aade10",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade14`](#insn-00aade14)

~~~json
{
  "source": "00aade14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade18`](#insn-00aade18)

~~~json
{
  "source": "00aade18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade1c`](#insn-00aade1c)

~~~json
{
  "source": "00aade1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
