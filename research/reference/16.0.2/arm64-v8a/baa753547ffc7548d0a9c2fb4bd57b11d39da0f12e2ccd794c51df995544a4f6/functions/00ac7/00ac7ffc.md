# 00ac7ffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ac7f8c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7f8c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-92a8216b7cbbcd5def309aaeb89f34b0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ac8ff0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac8ff0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-ed1d40dc94ad6cf2ecb46f2dc9471b2e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac7ffc",
  "name": "FUN_00ac7ffc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f2e2d247eccab25239394b787321cdd2c74044a1c7a470b99565eb0fba1b0d5",
  "source_text_sha256": "3f2e2d247eccab25239394b787321cdd2c74044a1c7a470b99565eb0fba1b0d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac7ffc",
        "00ac804f"
      ]
    ],
    "bytes_sha256": "20441bc77ddcd1ce410795e79e8453ce2826083bc07371311bea619d78a9cfe1",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0098dc5c](../0098d/0098dc5c.md)

## 呼び出し先

- [00459db4](../00459/00459db4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 423 bytes

~~~c

bool FUN_00ac7ffc(long param_1)

{
  int iVar1;
  
  iVar1 = *(int *)(param_1 + 0xa4);
  *(int *)(param_1 + 0xa4) = iVar1 + 1;
  if (0x17 < iVar1) {
    if (*(long **)(param_1 + 0x160) == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
      FUN_00459db4();
    }
    (**(code **)(**(long **)(param_1 + 0x160) + 0x30))();
    *(undefined1 *)(param_1 + 0xa0) = 0;
  }
  return 0x17 < iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac7ffc"></a> `00ac7ffc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ac8000"></a> `00ac8000` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac8004"></a> `00ac8004` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac8008"></a> `00ac8008` | `14 a4 40 b9` | ldr w20,[x0, #0xa4] | `FALL_THROUGH`
<a id="insn-00ac800c"></a> `00ac800c` | `88 06 00 11` | add w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00ac8010"></a> `00ac8010` | `9f 62 00 71` | cmp w20,#0x18 | `FALL_THROUGH`
<a id="insn-00ac8014"></a> `00ac8014` | `08 a4 00 b9` | str w8,[x0, #0xa4] | `FALL_THROUGH`
<a id="insn-00ac8018"></a> `00ac8018` | `0b 01 00 54` | b.lt 0x00ac8038 | `CONDITIONAL_JUMP`
<a id="insn-00ac801c"></a> `00ac801c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac8020"></a> `00ac8020` | `00 b0 40 f9` | ldr x0,[x0, #0x160] | `FALL_THROUGH`
<a id="insn-00ac8024"></a> `00ac8024` | `40 01 00 b4` | cbz x0,0x00ac804c | `CONDITIONAL_JUMP`
<a id="insn-00ac8028"></a> `00ac8028` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac802c"></a> `00ac802c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ac8030"></a> `00ac8030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac8034"></a> `00ac8034` | `7f 82 02 39` | strb wzr,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00ac8038"></a> `00ac8038` | `9f 5e 00 71` | cmp w20,#0x17 | `FALL_THROUGH`
<a id="insn-00ac803c"></a> `00ac803c` | `e0 d7 9f 1a` | cset w0,gt | `FALL_THROUGH`
<a id="insn-00ac8040"></a> `00ac8040` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac8044"></a> `00ac8044` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ac8048"></a> `00ac8048` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac804c"></a> `00ac804c` | `5a 47 e6 97` | bl 0x00459db4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac7ffc`](#insn-00ac7ffc) 範囲 `[['00ac7ffc', '00ac801b']]`
  - `CONDITIONAL_JUMP` [`00ac8018`](#insn-00ac8018) → [`00ac8038`](#insn-00ac8038)
  - `FALL_THROUGH` [`00ac8018`](#insn-00ac8018) → [`00ac801c`](#insn-00ac801c)
- ブロック [`00ac801c`](#insn-00ac801c) 範囲 `[['00ac801c', '00ac8027']]`
  - `CONDITIONAL_JUMP` [`00ac8024`](#insn-00ac8024) → [`00ac804c`](#insn-00ac804c)
  - `FALL_THROUGH` [`00ac8024`](#insn-00ac8024) → [`00ac8028`](#insn-00ac8028)
- ブロック [`00ac8028`](#insn-00ac8028) 範囲 `[['00ac8028', '00ac8037']]`
  - `FALL_THROUGH` [`00ac8034`](#insn-00ac8034) → [`00ac8038`](#insn-00ac8038)
- ブロック [`00ac8038`](#insn-00ac8038) 範囲 `[['00ac8038', '00ac804b']]`
- ブロック [`00ac804c`](#insn-00ac804c) 範囲 `[['00ac804c', '00ac804f']]`

## 命令位置別の参照

- [`00ac7ffc`](#insn-00ac7ffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8000`](#insn-00ac8000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8018`](#insn-00ac8018) → [`00ac8038`](#insn-00ac8038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8024`](#insn-00ac8024) → [`00ac804c`](#insn-00ac804c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8040`](#insn-00ac8040) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8044`](#insn-00ac8044) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac804c`](#insn-00ac804c) → [`00459db4`](../00459/00459db4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459db4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac7ffc`](#insn-00ac7ffc)

~~~json
{
  "source": "00ac7ffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8000`](#insn-00ac8000)

~~~json
{
  "source": "00ac8000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8018`](#insn-00ac8018)

~~~json
{
  "source": "00ac8018",
  "target": "00ac8038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8024`](#insn-00ac8024)

~~~json
{
  "source": "00ac8024",
  "target": "00ac804c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8040`](#insn-00ac8040)

~~~json
{
  "source": "00ac8040",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8044`](#insn-00ac8044)

~~~json
{
  "source": "00ac8044",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac804c`](#insn-00ac804c)

~~~json
{
  "source": "00ac804c",
  "target": "00459db4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
