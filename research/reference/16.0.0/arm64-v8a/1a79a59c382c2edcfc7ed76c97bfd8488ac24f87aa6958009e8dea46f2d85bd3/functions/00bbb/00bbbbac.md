# 00bbbbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-626916c6112225318d553617f362fcae)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbfd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-d70111b06c4db4bf025fb6efb495eee8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbbac",
  "name": "_ZN8firebase9messaging27IsRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "341bdc6da625b0e4790802aafb56753c3c77ec0ff56c0c868ffb25920accfcbc",
  "source_text_sha256": "341bdc6da625b0e4790802aafb56753c3c77ec0ff56c0c868ffb25920accfcbc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbbac",
        "00bbbc17"
      ]
    ],
    "bytes_sha256": "141e8c1e72d6a640272b260b9111f13644157f79934cc2c9fe012bde45bb3a9c",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a08](../00497/00497a08.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 539 bytes

~~~c

bool _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
                    /* try { // try from 00bbbbd0 to 00cbbc6f has its CatchHandler @ 00bbc5cc */
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    if (DAT_01125f60 == 0) {
      return true;
    }
  }
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
  cVar1 = FUN_00497a08(uVar2,DAT_01125f98,DAT_01125eb8);
  return cVar1 != '\0';
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbbac"></a> `00bbbbac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbbbb0"></a> `00bbbbb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbbb4"></a> `00bbbbb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbbb8"></a> `00bbbbb8` | `53 2b 00 d0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbbbc"></a> `00bbbbbc` | `60 b2 47 f9` | ldr x0,[x19, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbbbc0"></a> `00bbbbc0` | `20 01 00 b5` | cbnz x0,0x00bbbbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbc4"></a> `00bbbbc4` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbbbc8"></a> `00bbbbc8` | `00 20 21 91` | add x0,x0,#0x848 | `FALL_THROUGH`
<a id="insn-00bbbbcc"></a> `00bbbbcc` | `35 7b 02 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbd0"></a> `00bbbbd0` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbbbd4"></a> `00bbbbd4` | `00 dc 1c 91` | add x0,x0,#0x737 | `FALL_THROUGH`
<a id="insn-00bbbbd8"></a> `00bbbbd8` | `0a 7c 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbdc"></a> `00bbbbdc` | `60 b2 47 f9` | ldr x0,[x19, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbbbe0"></a> `00bbbbe0` | `80 01 00 b4` | cbz x0,0x00bbbc10 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbe4"></a> `00bbbbe4` | `27 7c 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbe8"></a> `00bbbbe8` | `48 2b 00 d0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbbec"></a> `00bbbbec` | `49 2b 00 d0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbbf0"></a> `00bbbbf0` | `01 cd 47 f9` | ldr x1,[x8, #0xf98] | `FALL_THROUGH`
<a id="insn-00bbbbf4"></a> `00bbbbf4` | `22 5d 47 f9` | ldr x2,[x9, #0xeb8] | `FALL_THROUGH`
<a id="insn-00bbbbf8"></a> `00bbbbf8` | `84 6f e3 97` | bl 0x00497a08 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbfc"></a> `00bbbbfc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbbc00"></a> `00bbbc00` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbbc04"></a> `00bbbc04` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbc08"></a> `00bbbc08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbbc0c"></a> `00bbbc0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbc10"></a> `00bbbc10` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbc14"></a> `00bbbc14` | `fc ff ff 17` | b 0x00bbbc04 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbbac`](#insn-00bbbbac) 範囲 `[['00bbbbac', '00bbbbc3']]`
  - `CONDITIONAL_JUMP` [`00bbbbc0`](#insn-00bbbbc0) → [`00bbbbe4`](#insn-00bbbbe4)
  - `FALL_THROUGH` [`00bbbbc0`](#insn-00bbbbc0) → [`00bbbbc4`](#insn-00bbbbc4)
- ブロック [`00bbbbc4`](#insn-00bbbbc4) 範囲 `[['00bbbbc4', '00bbbbcf']]`
  - `FALL_THROUGH` [`00bbbbcc`](#insn-00bbbbcc) → [`00bbbbd0`](#insn-00bbbbd0)
- ブロック [`00bbbbd0`](#insn-00bbbbd0) 範囲 `[['00bbbbd0', '00bbbbe3']]`
  - `CONDITIONAL_JUMP` [`00bbbbe0`](#insn-00bbbbe0) → [`00bbbc10`](#insn-00bbbc10)
  - `FALL_THROUGH` [`00bbbbe0`](#insn-00bbbbe0) → [`00bbbbe4`](#insn-00bbbbe4)
- ブロック [`00bbbbe4`](#insn-00bbbbe4) 範囲 `[['00bbbbe4', '00bbbc03']]`
  - `FALL_THROUGH` [`00bbbc00`](#insn-00bbbc00) → [`00bbbc04`](#insn-00bbbc04)
- ブロック [`00bbbc04`](#insn-00bbbc04) 範囲 `[['00bbbc04', '00bbbc0f']]`
- ブロック [`00bbbc10`](#insn-00bbbc10) 範囲 `[['00bbbc10', '00bbbc17']]`
  - `UNCONDITIONAL_JUMP` [`00bbbc14`](#insn-00bbbc14) → [`00bbbc04`](#insn-00bbbc04)

## 命令位置別の参照

- [`00bbbbac`](#insn-00bbbbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbb0`](#insn-00bbbbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbbc`](#insn-00bbbbbc) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbbc0`](#insn-00bbbbc0) → [`00bbbbe4`](#insn-00bbbbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbc8`](#insn-00bbbbc8) → `002a2848`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbbcc`](#insn-00bbbbcc) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbd4`](#insn-00bbbbd4) → `002b0737`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbbd8`](#insn-00bbbbd8) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbdc`](#insn-00bbbbdc) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbbe0`](#insn-00bbbbe0) → [`00bbbc10`](#insn-00bbbc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe4`](#insn-00bbbbe4) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf0`](#insn-00bbbbf0) → `01125f98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbbf4`](#insn-00bbbbf4) → `01125eb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbbf8`](#insn-00bbbbf8) → [`00497a08`](../00497/00497a08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a08` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc04`](#insn-00bbbc04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc14`](#insn-00bbbc14) → [`00bbbc04`](#insn-00bbbc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbbac`](#insn-00bbbbac)

~~~json
{
  "source": "00bbbbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbb0`](#insn-00bbbbb0)

~~~json
{
  "source": "00bbbbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbbc`](#insn-00bbbbbc)

~~~json
{
  "source": "00bbbbbc",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbbc0`](#insn-00bbbbc0)

~~~json
{
  "source": "00bbbbc0",
  "target": "00bbbbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbc8`](#insn-00bbbbc8)

~~~json
{
  "source": "00bbbbc8",
  "target": "002a2848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2848",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2848",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbbcc`](#insn-00bbbbcc)

~~~json
{
  "source": "00bbbbcc",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbd4`](#insn-00bbbbd4)

~~~json
{
  "source": "00bbbbd4",
  "target": "002b0737",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0737",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0737",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbbd8`](#insn-00bbbbd8)

~~~json
{
  "source": "00bbbbd8",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbdc`](#insn-00bbbbdc)

~~~json
{
  "source": "00bbbbdc",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbbe0`](#insn-00bbbbe0)

~~~json
{
  "source": "00bbbbe0",
  "target": "00bbbc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbe4`](#insn-00bbbbe4)

~~~json
{
  "source": "00bbbbe4",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbf0`](#insn-00bbbbf0)

~~~json
{
  "source": "00bbbbf0",
  "target": "01125f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbbf4`](#insn-00bbbbf4)

~~~json
{
  "source": "00bbbbf4",
  "target": "01125eb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125eb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbbf8`](#insn-00bbbbf8)

~~~json
{
  "source": "00bbbbf8",
  "target": "00497a08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc04`](#insn-00bbbc04)

~~~json
{
  "source": "00bbbc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc14`](#insn-00bbbc14)

~~~json
{
  "source": "00bbbc14",
  "target": "00bbbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
