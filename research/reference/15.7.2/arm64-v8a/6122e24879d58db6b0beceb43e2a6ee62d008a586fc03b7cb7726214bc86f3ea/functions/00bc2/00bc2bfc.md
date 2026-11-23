# 00bc2bfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bc2cc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2cc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-538b7f8697dffdfbb9f9e92a59278953)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2bfc",
  "name": "FUN_00bc2bfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c79c8f0013f2026a8b58687fdafb4fe53fd94b9ef65bec6438d74372d7b52f3b",
  "source_text_sha256": "c79c8f0013f2026a8b58687fdafb4fe53fd94b9ef65bec6438d74372d7b52f3b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2bfc",
        "00bc2c77"
      ]
    ],
    "bytes_sha256": "9fc546205aa5976404ff90dceced3701ee1a15dd1f00cf49dbfa366ed78084c2",
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

## 疑似コード / UTF-8 666 bytes

~~~c

byte FUN_00bc2bfc(long param_1)

{
  byte bVar1;
  long *plVar2;
  
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    plVar2 = *(long **)(param_1 + 0x18);
    *(undefined1 *)(param_1 + 0x20) = 1;
                    /* try { // try from 00bc2c30 to 00cc2c37 has its CatchHandler @ 00bc8844 */
    if ((*(byte *)((long)plVar2 + 10) & 3) == 2) {
      bVar1 = (**(code **)(*plVar2 + 8))(plVar2);
    }
    else {
      bVar1 = (*(byte *)((long)plVar2 + 10) & 3) == 0;
    }
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  else {
    bVar1 = 0;
  }
                    /* try { // try from 00bc2c64 to 00cc2ce3 has its CatchHandler @ 00bc89fc */
  return bVar1 & 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2bfc"></a> `00bc2bfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc2c00"></a> `00bc2c00` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc2c04"></a> `00bc2c04` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2c08"></a> `00bc2c08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bc2c0c"></a> `00bc2c0c` | `08 80 40 39` | ldrb w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2c10"></a> `00bc2c10` | `68 00 00 36` | tbz w8,#0x0,0x00bc2c1c | `CONDITIONAL_JUMP`
<a id="insn-00bc2c14"></a> `00bc2c14` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc2c18"></a> `00bc2c18` | `13 00 00 14` | b 0x00bc2c64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc2c1c"></a> `00bc2c1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc2c20"></a> `00bc2c20` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bc2c24"></a> `00bc2c24` | `09 80 00 39` | strb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2c28"></a> `00bc2c28` | `09 29 40 39` | ldrb w9,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bc2c2c"></a> `00bc2c2c` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bc2c30"></a> `00bc2c30` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bc2c34"></a> `00bc2c34` | `21 01 00 54` | b.ne 0x00bc2c58 | `CONDITIONAL_JUMP`
<a id="insn-00bc2c38"></a> `00bc2c38` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bc2c3c"></a> `00bc2c3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc2c40"></a> `00bc2c40` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2c44"></a> `00bc2c44` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2c48"></a> `00bc2c48` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bc2c4c"></a> `00bc2c4c` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00bc2c50"></a> `00bc2c50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc2c54"></a> `00bc2c54` | `03 00 00 14` | b 0x00bc2c60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc2c58"></a> `00bc2c58` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00bc2c5c"></a> `00bc2c5c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bc2c60"></a> `00bc2c60` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2c64"></a> `00bc2c64` | `00 01 00 12` | and w0,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc2c68"></a> `00bc2c68` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2c6c"></a> `00bc2c6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc2c70"></a> `00bc2c70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc2c74"></a> `00bc2c74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2bfc`](#insn-00bc2bfc) 範囲 `[['00bc2bfc', '00bc2c13']]`
  - `CONDITIONAL_JUMP` [`00bc2c10`](#insn-00bc2c10) → [`00bc2c1c`](#insn-00bc2c1c)
  - `FALL_THROUGH` [`00bc2c10`](#insn-00bc2c10) → [`00bc2c14`](#insn-00bc2c14)
- ブロック [`00bc2c14`](#insn-00bc2c14) 範囲 `[['00bc2c14', '00bc2c1b']]`
  - `UNCONDITIONAL_JUMP` [`00bc2c18`](#insn-00bc2c18) → [`00bc2c64`](#insn-00bc2c64)
- ブロック [`00bc2c1c`](#insn-00bc2c1c) 範囲 `[['00bc2c1c', '00bc2c2f']]`
  - `FALL_THROUGH` [`00bc2c2c`](#insn-00bc2c2c) → [`00bc2c30`](#insn-00bc2c30)
- ブロック [`00bc2c30`](#insn-00bc2c30) 範囲 `[['00bc2c30', '00bc2c37']]`
  - `CONDITIONAL_JUMP` [`00bc2c34`](#insn-00bc2c34) → [`00bc2c58`](#insn-00bc2c58)
  - `FALL_THROUGH` [`00bc2c34`](#insn-00bc2c34) → [`00bc2c38`](#insn-00bc2c38)
- ブロック [`00bc2c38`](#insn-00bc2c38) 範囲 `[['00bc2c38', '00bc2c57']]`
  - `UNCONDITIONAL_JUMP` [`00bc2c54`](#insn-00bc2c54) → [`00bc2c60`](#insn-00bc2c60)
- ブロック [`00bc2c58`](#insn-00bc2c58) 範囲 `[['00bc2c58', '00bc2c5f']]`
  - `FALL_THROUGH` [`00bc2c5c`](#insn-00bc2c5c) → [`00bc2c60`](#insn-00bc2c60)
- ブロック [`00bc2c60`](#insn-00bc2c60) 範囲 `[['00bc2c60', '00bc2c63']]`
  - `FALL_THROUGH` [`00bc2c60`](#insn-00bc2c60) → [`00bc2c64`](#insn-00bc2c64)
- ブロック [`00bc2c64`](#insn-00bc2c64) 範囲 `[['00bc2c64', '00bc2c77']]`

## 命令位置別の参照

- [`00bc2c00`](#insn-00bc2c00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c04`](#insn-00bc2c04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c10`](#insn-00bc2c10) → [`00bc2c1c`](#insn-00bc2c1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c18`](#insn-00bc2c18) → [`00bc2c64`](#insn-00bc2c64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c34`](#insn-00bc2c34) → [`00bc2c58`](#insn-00bc2c58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c54`](#insn-00bc2c54) → [`00bc2c60`](#insn-00bc2c60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c68`](#insn-00bc2c68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2c6c`](#insn-00bc2c6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2c00`](#insn-00bc2c00)

~~~json
{
  "source": "00bc2c00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c04`](#insn-00bc2c04)

~~~json
{
  "source": "00bc2c04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c10`](#insn-00bc2c10)

~~~json
{
  "source": "00bc2c10",
  "target": "00bc2c1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c18`](#insn-00bc2c18)

~~~json
{
  "source": "00bc2c18",
  "target": "00bc2c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c34`](#insn-00bc2c34)

~~~json
{
  "source": "00bc2c34",
  "target": "00bc2c58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c54`](#insn-00bc2c54)

~~~json
{
  "source": "00bc2c54",
  "target": "00bc2c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c68`](#insn-00bc2c68)

~~~json
{
  "source": "00bc2c68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2c6c`](#insn-00bc2c6c)

~~~json
{
  "source": "00bc2c6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
