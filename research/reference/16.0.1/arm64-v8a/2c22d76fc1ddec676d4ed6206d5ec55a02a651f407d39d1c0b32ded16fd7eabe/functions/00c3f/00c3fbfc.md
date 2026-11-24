# 00c3fbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3f7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0044.md#compare-8d3ff68ca0fb55842c9a86ff27067f1f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c3fc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0045.md#compare-243da58965fd549b4e31bb6895d81758)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3fbfc",
  "name": "FUN_00c3fbfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc",
  "source_text_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3fbfc",
        "00c3fc77"
      ]
    ],
    "bytes_sha256": "41a2473a3e65e0bffeecbb9f13280917b26f22485b7f8d704bf6763ed7698d9f",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 583 bytes

~~~c

byte FUN_00c3fbfc(long param_1)

{
  ushort uVar1;
  byte bVar2;
  long *plVar3;
  
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    plVar3 = *(long **)(param_1 + 0x18);
    *(undefined1 *)(param_1 + 0x20) = 1;
    uVar1 = *(ushort *)((long)plVar3 + 9) >> 10 & 3;
                    /* try { // try from 00c3fc34 to 00d3fcbb has its CatchHandler @ 00c3fda0 */
    if (uVar1 == 2) {
      bVar2 = (**(code **)(*plVar3 + 0x10))(plVar3);
    }
    else {
      bVar2 = uVar1 == 0;
    }
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  else {
    bVar2 = 0;
  }
  return bVar2 & 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c3fbfc"></a> `00c3fbfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3fc00"></a> `00c3fc00` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00c3fc04"></a> `00c3fc04` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fc08"></a> `00c3fc08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c3fc0c"></a> `00c3fc0c` | `08 80 40 39` | ldrb w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fc10"></a> `00c3fc10` | `68 00 00 36` | tbz w8,#0x0,0x00c3fc1c | `CONDITIONAL_JUMP`
<a id="insn-00c3fc14"></a> `00c3fc14` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00c3fc18"></a> `00c3fc18` | `13 00 00 14` | b 0x00c3fc64 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fc1c"></a> `00c3fc1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc20"></a> `00c3fc20` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c3fc24"></a> `00c3fc24` | `09 80 00 39` | strb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fc28"></a> `00c3fc28` | `09 91 40 78` | ldurh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00c3fc2c"></a> `00c3fc2c` | `29 2d 0a 53` | ubfx w9,w9,#0xa,#0x2 | `FALL_THROUGH`
<a id="insn-00c3fc30"></a> `00c3fc30` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-00c3fc34"></a> `00c3fc34` | `21 01 00 54` | b.ne 0x00c3fc58 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc38"></a> `00c3fc38` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00c3fc3c"></a> `00c3fc3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c3fc40"></a> `00c3fc40` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fc44"></a> `00c3fc44` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c3fc48"></a> `00c3fc48` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c3fc4c"></a> `00c3fc4c` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00c3fc50"></a> `00c3fc50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c3fc54"></a> `00c3fc54` | `03 00 00 14` | b 0x00c3fc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fc58"></a> `00c3fc58` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00c3fc5c"></a> `00c3fc5c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c3fc60"></a> `00c3fc60` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fc64"></a> `00c3fc64` | `00 01 00 12` | and w0,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc68"></a> `00c3fc68` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fc6c"></a> `00c3fc6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00c3fc70"></a> `00c3fc70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3fc74"></a> `00c3fc74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3fbfc`](#insn-00c3fbfc) 範囲 `[['00c3fbfc', '00c3fc13']]`
  - `CONDITIONAL_JUMP` [`00c3fc10`](#insn-00c3fc10) → [`00c3fc1c`](#insn-00c3fc1c)
  - `FALL_THROUGH` [`00c3fc10`](#insn-00c3fc10) → [`00c3fc14`](#insn-00c3fc14)
- ブロック [`00c3fc14`](#insn-00c3fc14) 範囲 `[['00c3fc14', '00c3fc1b']]`
  - `UNCONDITIONAL_JUMP` [`00c3fc18`](#insn-00c3fc18) → [`00c3fc64`](#insn-00c3fc64)
- ブロック [`00c3fc1c`](#insn-00c3fc1c) 範囲 `[['00c3fc1c', '00c3fc33']]`
  - `FALL_THROUGH` [`00c3fc30`](#insn-00c3fc30) → [`00c3fc34`](#insn-00c3fc34)
- ブロック [`00c3fc34`](#insn-00c3fc34) 範囲 `[['00c3fc34', '00c3fc37']]`
  - `CONDITIONAL_JUMP` [`00c3fc34`](#insn-00c3fc34) → [`00c3fc58`](#insn-00c3fc58)
  - `FALL_THROUGH` [`00c3fc34`](#insn-00c3fc34) → [`00c3fc38`](#insn-00c3fc38)
- ブロック [`00c3fc38`](#insn-00c3fc38) 範囲 `[['00c3fc38', '00c3fc57']]`
  - `UNCONDITIONAL_JUMP` [`00c3fc54`](#insn-00c3fc54) → [`00c3fc60`](#insn-00c3fc60)
- ブロック [`00c3fc58`](#insn-00c3fc58) 範囲 `[['00c3fc58', '00c3fc5f']]`
  - `FALL_THROUGH` [`00c3fc5c`](#insn-00c3fc5c) → [`00c3fc60`](#insn-00c3fc60)
- ブロック [`00c3fc60`](#insn-00c3fc60) 範囲 `[['00c3fc60', '00c3fc63']]`
  - `FALL_THROUGH` [`00c3fc60`](#insn-00c3fc60) → [`00c3fc64`](#insn-00c3fc64)
- ブロック [`00c3fc64`](#insn-00c3fc64) 範囲 `[['00c3fc64', '00c3fc77']]`

## 命令位置別の参照

- [`00c3fc00`](#insn-00c3fc00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc04`](#insn-00c3fc04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc10`](#insn-00c3fc10) → [`00c3fc1c`](#insn-00c3fc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc18`](#insn-00c3fc18) → [`00c3fc64`](#insn-00c3fc64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc34`](#insn-00c3fc34) → [`00c3fc58`](#insn-00c3fc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc54`](#insn-00c3fc54) → [`00c3fc60`](#insn-00c3fc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc68`](#insn-00c3fc68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc6c`](#insn-00c3fc6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3fc00`](#insn-00c3fc00)

~~~json
{
  "source": "00c3fc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc04`](#insn-00c3fc04)

~~~json
{
  "source": "00c3fc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc10`](#insn-00c3fc10)

~~~json
{
  "source": "00c3fc10",
  "target": "00c3fc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc18`](#insn-00c3fc18)

~~~json
{
  "source": "00c3fc18",
  "target": "00c3fc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc34`](#insn-00c3fc34)

~~~json
{
  "source": "00c3fc34",
  "target": "00c3fc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc54`](#insn-00c3fc54)

~~~json
{
  "source": "00c3fc54",
  "target": "00c3fc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc68`](#insn-00c3fc68)

~~~json
{
  "source": "00c3fc68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc6c`](#insn-00c3fc6c)

~~~json
{
  "source": "00c3fc6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
