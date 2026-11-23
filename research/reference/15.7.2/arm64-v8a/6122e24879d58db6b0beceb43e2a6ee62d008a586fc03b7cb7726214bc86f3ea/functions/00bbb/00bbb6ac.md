# 00bbb6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb774`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb774.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-852339f0928a98b3d7d53d66b678b94c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb6ac",
  "name": "FUN_00bbb6ac",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57e270e480ce76722c3606b9ee7de6cb723ac26108a284bcd7d53852ab9c22e6",
  "source_text_sha256": "57e270e480ce76722c3606b9ee7de6cb723ac26108a284bcd7d53852ab9c22e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb6ac",
        "00bbb733"
      ]
    ],
    "bytes_sha256": "4e20a95870b991403b4d30c9a5f6c8f19f30c0ed824b700deb3efc00100e63e3",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1535 bytes

~~~c

void FUN_00bbb6ac(long param_1,long param_2,long param_3,undefined4 param_4)

{
                    /* catch() { ... } // from try @ 00bbb514 with catch @ 00bbb6b4 */
  if (*(long *)(param_1 + 8) == *(long *)(*(long *)(param_2 + 0x10) + 8)) {
                    /* catch() { ... } // from try @ 00bbb504 with catch @ 00bbb6cc */
    if (*(int *)(param_2 + 0x3c) == 0) {
                    /* catch() { ... } // from try @ 00bbb3cc with catch @ 00bbb710 */
      *(undefined4 *)(param_2 + 0x30) = param_4;
                    /* catch() { ... } // from try @ 00bbb288 with catch @ 00bbb714 */
      *(undefined4 *)(param_2 + 0x3c) = 1;
      *(long *)(param_2 + 0x20) = param_3;
      *(undefined8 *)(param_2 + 0x28) = *(undefined8 *)(param_2 + 0x50);
      return;
    }
                    /* catch() { ... } // from try @ 00bbb4f8 with catch @ 00bbb6e0 */
                    /* catch() { ... } // from try @ 00bbb3e8 with catch @ 00bbb6e4 */
    if ((*(long *)(param_2 + 0x28) != *(long *)(param_2 + 0x50)) ||
       (*(long *)(param_2 + 0x20) != param_3)) {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
                    /* catch() { ... } // from try @ 00bbb3d8 with catch @ 00bbb6fc */
      *(undefined4 *)(param_2 + 0x30) = 2;
      *(undefined1 *)(param_2 + 0x4e) = 1;
      return;
    }
    if (*(int *)(param_2 + 0x30) == 2) {
                    /* catch() { ... } // from try @ 00bbb278 with catch @ 00bbb72c */
      *(undefined4 *)(param_2 + 0x30) = param_4;
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb6ac"></a> `00bbb6ac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbb6b0"></a> `00bbb6b0` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb6b4"></a> `00bbb6b4` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb6b8"></a> `00bbb6b8` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb6bc"></a> `00bbb6bc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbb6c0"></a> `00bbb6c0` | `40 00 00 54` | b.eq 0x00bbb6c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb6c4"></a> `00bbb6c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb6c8"></a> `00bbb6c8` | `28 3c 40 b9` | ldr w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb6cc"></a> `00bbb6cc` | `e8 01 00 34` | cbz w8,0x00bbb708 | `CONDITIONAL_JUMP`
<a id="insn-00bbb6d0"></a> `00bbb6d0` | `29 14 40 f9` | ldr x9,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb6d4"></a> `00bbb6d4` | `2a 28 40 f9` | ldr x10,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb6d8"></a> `00bbb6d8` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbb6dc"></a> `00bbb6dc` | `81 00 00 54` | b.ne 0x00bbb6ec | `CONDITIONAL_JUMP`
<a id="insn-00bbb6e0"></a> `00bbb6e0` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb6e4"></a> `00bbb6e4` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bbb6e8"></a> `00bbb6e8` | `c0 01 00 54` | b.eq 0x00bbb720 | `CONDITIONAL_JUMP`
<a id="insn-00bbb6ec"></a> `00bbb6ec` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb6f0"></a> `00bbb6f0` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb6f4"></a> `00bbb6f4` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb6f8"></a> `00bbb6f8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb6fc"></a> `00bbb6fc` | `29 30 00 b9` | str w9,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb700"></a> `00bbb700` | `28 38 01 39` | strb w8,[x1, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbb704"></a> `00bbb704` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb708"></a> `00bbb708` | `28 28 40 f9` | ldr x8,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb70c"></a> `00bbb70c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb710"></a> `00bbb710` | `23 30 00 b9` | str w3,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb714"></a> `00bbb714` | `29 3c 00 b9` | str w9,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb718"></a> `00bbb718` | `22 20 02 a9` | stp x2,x8,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb71c"></a> `00bbb71c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb720"></a> `00bbb720` | `28 30 40 b9` | ldr w8,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb724"></a> `00bbb724` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb728"></a> `00bbb728` | `e1 fc ff 54` | b.ne 0x00bbb6c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb72c"></a> `00bbb72c` | `23 30 00 b9` | str w3,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb730"></a> `00bbb730` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb6ac`](#insn-00bbb6ac) 範囲 `[['00bbb6ac', '00bbb6b3']]`
  - `FALL_THROUGH` [`00bbb6b0`](#insn-00bbb6b0) → [`00bbb6b4`](#insn-00bbb6b4)
- ブロック [`00bbb6b4`](#insn-00bbb6b4) 範囲 `[['00bbb6b4', '00bbb6c3']]`
  - `CONDITIONAL_JUMP` [`00bbb6c0`](#insn-00bbb6c0) → [`00bbb6c8`](#insn-00bbb6c8)
  - `FALL_THROUGH` [`00bbb6c0`](#insn-00bbb6c0) → [`00bbb6c4`](#insn-00bbb6c4)
- ブロック [`00bbb6c4`](#insn-00bbb6c4) 範囲 `[['00bbb6c4', '00bbb6c7']]`
- ブロック [`00bbb6c8`](#insn-00bbb6c8) 範囲 `[['00bbb6c8', '00bbb6cb']]`
  - `FALL_THROUGH` [`00bbb6c8`](#insn-00bbb6c8) → [`00bbb6cc`](#insn-00bbb6cc)
- ブロック [`00bbb6cc`](#insn-00bbb6cc) 範囲 `[['00bbb6cc', '00bbb6cf']]`
  - `CONDITIONAL_JUMP` [`00bbb6cc`](#insn-00bbb6cc) → [`00bbb708`](#insn-00bbb708)
  - `FALL_THROUGH` [`00bbb6cc`](#insn-00bbb6cc) → [`00bbb6d0`](#insn-00bbb6d0)
- ブロック [`00bbb6d0`](#insn-00bbb6d0) 範囲 `[['00bbb6d0', '00bbb6df']]`
  - `CONDITIONAL_JUMP` [`00bbb6dc`](#insn-00bbb6dc) → [`00bbb6ec`](#insn-00bbb6ec)
  - `FALL_THROUGH` [`00bbb6dc`](#insn-00bbb6dc) → [`00bbb6e0`](#insn-00bbb6e0)
- ブロック [`00bbb6e0`](#insn-00bbb6e0) 範囲 `[['00bbb6e0', '00bbb6e3']]`
  - `FALL_THROUGH` [`00bbb6e0`](#insn-00bbb6e0) → [`00bbb6e4`](#insn-00bbb6e4)
- ブロック [`00bbb6e4`](#insn-00bbb6e4) 範囲 `[['00bbb6e4', '00bbb6eb']]`
  - `CONDITIONAL_JUMP` [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb720`](#insn-00bbb720)
  - `FALL_THROUGH` [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb6ec`](#insn-00bbb6ec)
- ブロック [`00bbb6ec`](#insn-00bbb6ec) 範囲 `[['00bbb6ec', '00bbb6fb']]`
  - `FALL_THROUGH` [`00bbb6f8`](#insn-00bbb6f8) → [`00bbb6fc`](#insn-00bbb6fc)
- ブロック [`00bbb6fc`](#insn-00bbb6fc) 範囲 `[['00bbb6fc', '00bbb707']]`
- ブロック [`00bbb708`](#insn-00bbb708) 範囲 `[['00bbb708', '00bbb70f']]`
  - `FALL_THROUGH` [`00bbb70c`](#insn-00bbb70c) → [`00bbb710`](#insn-00bbb710)
- ブロック [`00bbb710`](#insn-00bbb710) 範囲 `[['00bbb710', '00bbb713']]`
  - `FALL_THROUGH` [`00bbb710`](#insn-00bbb710) → [`00bbb714`](#insn-00bbb714)
- ブロック [`00bbb714`](#insn-00bbb714) 範囲 `[['00bbb714', '00bbb71f']]`
- ブロック [`00bbb720`](#insn-00bbb720) 範囲 `[['00bbb720', '00bbb72b']]`
  - `CONDITIONAL_JUMP` [`00bbb728`](#insn-00bbb728) → [`00bbb6c4`](#insn-00bbb6c4)
  - `FALL_THROUGH` [`00bbb728`](#insn-00bbb728) → [`00bbb72c`](#insn-00bbb72c)
- ブロック [`00bbb72c`](#insn-00bbb72c) 範囲 `[['00bbb72c', '00bbb733']]`

## 命令位置別の参照

- [`00bbb6c0`](#insn-00bbb6c0) → [`00bbb6c8`](#insn-00bbb6c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6cc`](#insn-00bbb6cc) → [`00bbb708`](#insn-00bbb708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6dc`](#insn-00bbb6dc) → [`00bbb6ec`](#insn-00bbb6ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb720`](#insn-00bbb720) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb728`](#insn-00bbb728) → [`00bbb6c4`](#insn-00bbb6c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb6c0`](#insn-00bbb6c0)

~~~json
{
  "source": "00bbb6c0",
  "target": "00bbb6c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6cc`](#insn-00bbb6cc)

~~~json
{
  "source": "00bbb6cc",
  "target": "00bbb708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6dc`](#insn-00bbb6dc)

~~~json
{
  "source": "00bbb6dc",
  "target": "00bbb6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6e8`](#insn-00bbb6e8)

~~~json
{
  "source": "00bbb6e8",
  "target": "00bbb720",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb728`](#insn-00bbb728)

~~~json
{
  "source": "00bbb728",
  "target": "00bbb6c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
