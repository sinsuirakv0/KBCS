# 004bbbac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004bbbac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bbbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0003.md#compare-1bb189eb07547a55f87fa71f7c9dfc82)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `004bbbac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbbac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0003.md#compare-398a6678a4e390dc46f2531ac66bd557)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "_ZN5Botan9Power_Mod11window_bitsEmmNS0_11Usage_HintsE",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bbad264736ce2902588b97bd8bfe144a275970b79279062d89cd280ad8e554d",
  "source_text_sha256": "0bbad264736ce2902588b97bd8bfe144a275970b79279062d89cd280ad8e554d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bbbac",
        "004bbc2f"
      ]
    ],
    "bytes_sha256": "27fbfd4128aed2f1b61b6089488e209ab85e58989b2c615cef3c4ef9eccc17f6",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
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

## 疑似コード / UTF-8 805 bytes

~~~c

long _ZN5Botan9Power_Mod11window_bitsEmmNS0_11Usage_HintsE
               (ulong param_1,undefined8 param_2,uint param_3)

{
  long lVar1;
  undefined *puVar2;
  
  if (param_1 == 0) {
LAB_004bbbd8:
    lVar1 = 1;
  }
  else {
    if (param_1 < 0x59a) {
      if (param_1 < 0x21b) {
        if (param_1 < 0xc5) {
          if (param_1 < 0x46) {
            if (param_1 < 0x19) goto LAB_004bbbd8;
            puVar2 = &UNK_002b99b8;
          }
          else {
            puVar2 = &UNK_002b99a8;
          }
        }
        else {
          puVar2 = &UNK_002b9998;
        }
      }
      else {
        puVar2 = &UNK_002b9988;
      }
    }
    else {
      puVar2 = &UNK_002b9978;
    }
    lVar1 = *(long *)(puVar2 + 8) + 1;
  }
  return lVar1 + (ulong)((param_3 & 1) << 1 | param_3 >> 10 & 1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bbbac"></a> `004bbbac` | `60 01 00 b4` | cbz x0,0x004bbbd8 | `CONDITIONAL_JUMP`
<a id="insn-004bbbb0"></a> `004bbbb0` | `1f 64 16 f1` | cmp x0,#0x599 | `FALL_THROUGH`
<a id="insn-004bbbb4"></a> `004bbbb4` | `68 01 00 54` | b.hi 0x004bbbe0 | `CONDITIONAL_JUMP`
<a id="insn-004bbbb8"></a> `004bbbb8` | `1f 68 08 f1` | cmp x0,#0x21a | `FALL_THROUGH`
<a id="insn-004bbbbc"></a> `004bbbbc` | `88 01 00 54` | b.hi 0x004bbbec | `CONDITIONAL_JUMP`
<a id="insn-004bbbc0"></a> `004bbbc0` | `1f 10 03 f1` | cmp x0,#0xc4 | `FALL_THROUGH`
<a id="insn-004bbbc4"></a> `004bbbc4` | `a8 01 00 54` | b.hi 0x004bbbf8 | `CONDITIONAL_JUMP`
<a id="insn-004bbbc8"></a> `004bbbc8` | `1f 14 01 f1` | cmp x0,#0x45 | `FALL_THROUGH`
<a id="insn-004bbbcc"></a> `004bbbcc` | `c8 01 00 54` | b.hi 0x004bbc04 | `CONDITIONAL_JUMP`
<a id="insn-004bbbd0"></a> `004bbbd0` | `1f 64 00 f1` | cmp x0,#0x19 | `FALL_THROUGH`
<a id="insn-004bbbd4"></a> `004bbbd4` | `e2 01 00 54` | b.cs 0x004bbc10 | `CONDITIONAL_JUMP`
<a id="insn-004bbbd8"></a> `004bbbd8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004bbbdc"></a> `004bbbdc` | `11 00 00 14` | b 0x004bbc20 | `UNCONDITIONAL_JUMP`
<a id="insn-004bbbe0"></a> `004bbbe0` | `e8 ef ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-004bbbe4"></a> `004bbbe4` | `08 e1 25 91` | add x8,x8,#0x978 | `FALL_THROUGH`
<a id="insn-004bbbe8"></a> `004bbbe8` | `0c 00 00 14` | b 0x004bbc18 | `UNCONDITIONAL_JUMP`
<a id="insn-004bbbec"></a> `004bbbec` | `e8 ef ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-004bbbf0"></a> `004bbbf0` | `08 21 26 91` | add x8,x8,#0x988 | `FALL_THROUGH`
<a id="insn-004bbbf4"></a> `004bbbf4` | `09 00 00 14` | b 0x004bbc18 | `UNCONDITIONAL_JUMP`
<a id="insn-004bbbf8"></a> `004bbbf8` | `e8 ef ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-004bbbfc"></a> `004bbbfc` | `08 61 26 91` | add x8,x8,#0x998 | `FALL_THROUGH`
<a id="insn-004bbc00"></a> `004bbc00` | `06 00 00 14` | b 0x004bbc18 | `UNCONDITIONAL_JUMP`
<a id="insn-004bbc04"></a> `004bbc04` | `e8 ef ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-004bbc08"></a> `004bbc08` | `08 a1 26 91` | add x8,x8,#0x9a8 | `FALL_THROUGH`
<a id="insn-004bbc0c"></a> `004bbc0c` | `03 00 00 14` | b 0x004bbc18 | `UNCONDITIONAL_JUMP`
<a id="insn-004bbc10"></a> `004bbc10` | `e8 ef ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-004bbc14"></a> `004bbc14` | `08 e1 26 91` | add x8,x8,#0x9b8 | `FALL_THROUGH`
<a id="insn-004bbc18"></a> `004bbc18` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004bbc1c"></a> `004bbc1c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004bbc20"></a> `004bbc20` | `49 00 1f 53` | ubfiz w9,w2,#0x1,#0x1 | `FALL_THROUGH`
<a id="insn-004bbc24"></a> `004bbc24` | `49 28 0a 33` | bfxil w9,w2,#0xa,#0x1 | `FALL_THROUGH`
<a id="insn-004bbc28"></a> `004bbc28` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-004bbc2c"></a> `004bbc2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bbbac`](#insn-004bbbac) 範囲 `[['004bbbac', '004bbbaf']]`
  - `CONDITIONAL_JUMP` [`004bbbac`](#insn-004bbbac) → [`004bbbd8`](#insn-004bbbd8)
  - `FALL_THROUGH` [`004bbbac`](#insn-004bbbac) → [`004bbbb0`](#insn-004bbbb0)
- ブロック [`004bbbb0`](#insn-004bbbb0) 範囲 `[['004bbbb0', '004bbbb7']]`
  - `CONDITIONAL_JUMP` [`004bbbb4`](#insn-004bbbb4) → [`004bbbe0`](#insn-004bbbe0)
  - `FALL_THROUGH` [`004bbbb4`](#insn-004bbbb4) → [`004bbbb8`](#insn-004bbbb8)
- ブロック [`004bbbb8`](#insn-004bbbb8) 範囲 `[['004bbbb8', '004bbbbf']]`
  - `CONDITIONAL_JUMP` [`004bbbbc`](#insn-004bbbbc) → [`004bbbec`](#insn-004bbbec)
  - `FALL_THROUGH` [`004bbbbc`](#insn-004bbbbc) → [`004bbbc0`](#insn-004bbbc0)
- ブロック [`004bbbc0`](#insn-004bbbc0) 範囲 `[['004bbbc0', '004bbbc7']]`
  - `CONDITIONAL_JUMP` [`004bbbc4`](#insn-004bbbc4) → [`004bbbf8`](#insn-004bbbf8)
  - `FALL_THROUGH` [`004bbbc4`](#insn-004bbbc4) → [`004bbbc8`](#insn-004bbbc8)
- ブロック [`004bbbc8`](#insn-004bbbc8) 範囲 `[['004bbbc8', '004bbbcf']]`
  - `CONDITIONAL_JUMP` [`004bbbcc`](#insn-004bbbcc) → [`004bbc04`](#insn-004bbc04)
  - `FALL_THROUGH` [`004bbbcc`](#insn-004bbbcc) → [`004bbbd0`](#insn-004bbbd0)
- ブロック [`004bbbd0`](#insn-004bbbd0) 範囲 `[['004bbbd0', '004bbbd7']]`
  - `CONDITIONAL_JUMP` [`004bbbd4`](#insn-004bbbd4) → [`004bbc10`](#insn-004bbc10)
  - `FALL_THROUGH` [`004bbbd4`](#insn-004bbbd4) → [`004bbbd8`](#insn-004bbbd8)
- ブロック [`004bbbd8`](#insn-004bbbd8) 範囲 `[['004bbbd8', '004bbbdf']]`
  - `UNCONDITIONAL_JUMP` [`004bbbdc`](#insn-004bbbdc) → [`004bbc20`](#insn-004bbc20)
- ブロック [`004bbbe0`](#insn-004bbbe0) 範囲 `[['004bbbe0', '004bbbeb']]`
  - `UNCONDITIONAL_JUMP` [`004bbbe8`](#insn-004bbbe8) → [`004bbc18`](#insn-004bbc18)
- ブロック [`004bbbec`](#insn-004bbbec) 範囲 `[['004bbbec', '004bbbf7']]`
  - `UNCONDITIONAL_JUMP` [`004bbbf4`](#insn-004bbbf4) → [`004bbc18`](#insn-004bbc18)
- ブロック [`004bbbf8`](#insn-004bbbf8) 範囲 `[['004bbbf8', '004bbc03']]`
  - `UNCONDITIONAL_JUMP` [`004bbc00`](#insn-004bbc00) → [`004bbc18`](#insn-004bbc18)
- ブロック [`004bbc04`](#insn-004bbc04) 範囲 `[['004bbc04', '004bbc0f']]`
  - `UNCONDITIONAL_JUMP` [`004bbc0c`](#insn-004bbc0c) → [`004bbc18`](#insn-004bbc18)
- ブロック [`004bbc10`](#insn-004bbc10) 範囲 `[['004bbc10', '004bbc17']]`
  - `FALL_THROUGH` [`004bbc14`](#insn-004bbc14) → [`004bbc18`](#insn-004bbc18)
- ブロック [`004bbc18`](#insn-004bbc18) 範囲 `[['004bbc18', '004bbc1f']]`
  - `FALL_THROUGH` [`004bbc1c`](#insn-004bbc1c) → [`004bbc20`](#insn-004bbc20)
- ブロック [`004bbc20`](#insn-004bbc20) 範囲 `[['004bbc20', '004bbc2f']]`

## 命令位置別の参照

- [`004bbbac`](#insn-004bbbac) → [`004bbbd8`](#insn-004bbbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbb4`](#insn-004bbbb4) → [`004bbbe0`](#insn-004bbbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbbc`](#insn-004bbbbc) → [`004bbbec`](#insn-004bbbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbc4`](#insn-004bbbc4) → [`004bbbf8`](#insn-004bbbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbcc`](#insn-004bbbcc) → [`004bbc04`](#insn-004bbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbd4`](#insn-004bbbd4) → [`004bbc10`](#insn-004bbc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbdc`](#insn-004bbbdc) → [`004bbc20`](#insn-004bbc20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbe8`](#insn-004bbbe8) → [`004bbc18`](#insn-004bbc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbf4`](#insn-004bbbf4) → [`004bbc18`](#insn-004bbc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc00`](#insn-004bbc00) → [`004bbc18`](#insn-004bbc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc0c`](#insn-004bbc0c) → [`004bbc18`](#insn-004bbc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc18`](#insn-004bbc18) → `002b99c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`004bbc18`](#insn-004bbc18) → `002b99b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`004bbc18`](#insn-004bbc18) → `002b99a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`004bbc18`](#insn-004bbc18) → `002b9990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`004bbc18`](#insn-004bbc18) → `002b9980`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bbbac`](#insn-004bbbac)

~~~json
{
  "source": "004bbbac",
  "target": "004bbbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbb4`](#insn-004bbbb4)

~~~json
{
  "source": "004bbbb4",
  "target": "004bbbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbbc`](#insn-004bbbbc)

~~~json
{
  "source": "004bbbbc",
  "target": "004bbbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbc4`](#insn-004bbbc4)

~~~json
{
  "source": "004bbbc4",
  "target": "004bbbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbcc`](#insn-004bbbcc)

~~~json
{
  "source": "004bbbcc",
  "target": "004bbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbd4`](#insn-004bbbd4)

~~~json
{
  "source": "004bbbd4",
  "target": "004bbc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbdc`](#insn-004bbbdc)

~~~json
{
  "source": "004bbbdc",
  "target": "004bbc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbe8`](#insn-004bbbe8)

~~~json
{
  "source": "004bbbe8",
  "target": "004bbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbf4`](#insn-004bbbf4)

~~~json
{
  "source": "004bbbf4",
  "target": "004bbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc00`](#insn-004bbc00)

~~~json
{
  "source": "004bbc00",
  "target": "004bbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc0c`](#insn-004bbc0c)

~~~json
{
  "source": "004bbc0c",
  "target": "004bbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b99c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b99c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0200000000000000",
  "capture_start": "002b99c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b99b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b99b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0300000000000000",
  "capture_start": "002b99b0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b99a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b99a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0400000000000000",
  "capture_start": "002b99a0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b9990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9990",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0600000000000000",
  "capture_start": "002b9990",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b9980",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9980",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0700000000000000",
  "capture_start": "002b9980",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
