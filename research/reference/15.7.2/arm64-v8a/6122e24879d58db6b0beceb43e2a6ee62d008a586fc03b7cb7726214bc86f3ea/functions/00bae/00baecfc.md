# 00baecfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baedc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baedc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-d9b5193dc229d47e684e6753ea7810e5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baecfc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d102170e09986169a85fffc09b45abbee3a6b1a447f29e8017a0ccc921777949",
  "source_text_sha256": "d102170e09986169a85fffc09b45abbee3a6b1a447f29e8017a0ccc921777949",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baecfc",
        "00baed6b"
      ]
    ],
    "bytes_sha256": "f57f9806b4dc0196ad4c4fe2fe925fa45b67d8983ef3c7353b7ef0b6da4ba962",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae630](../00bae/00bae630.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baec60 with catch @ 00baed18 */
                    /* catch() { ... } // from try @ 00baec54 with catch @ 00baed30 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* catch() { ... } // from try @ 00baec28 with catch @ 00baed48 */
  FUN_00bae630(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
                    /* catch() { ... } // from try @ 00baebfc with catch @ 00baed58 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baecfc"></a> `00baecfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baed00"></a> `00baed00` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baed04"></a> `00baed04` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed08"></a> `00baed08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed0c"></a> `00baed0c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baed10"></a> `00baed10` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baed14"></a> `00baed14` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baed18"></a> `00baed18` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baed1c"></a> `00baed1c` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baed20"></a> `00baed20` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baed24"></a> `00baed24` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baed28"></a> `00baed28` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baed2c"></a> `00baed2c` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baed30"></a> `00baed30` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baed34"></a> `00baed34` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baed38"></a> `00baed38` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baed3c"></a> `00baed3c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baed40"></a> `00baed40` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baed44"></a> `00baed44` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baed48"></a> `00baed48` | `3a fe ff 97` | bl 0x00bae630 | `UNCONDITIONAL_CALL`
<a id="insn-00baed4c"></a> `00baed4c` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baed50"></a> `00baed50` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baed54"></a> `00baed54` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baed58"></a> `00baed58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed5c"></a> `00baed5c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed60"></a> `00baed60` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baed64"></a> `00baed64` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baed68"></a> `00baed68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baecfc`](#insn-00baecfc) 範囲 `[['00baecfc', '00baed17']]`
  - `FALL_THROUGH` [`00baed14`](#insn-00baed14) → [`00baed18`](#insn-00baed18)
- ブロック [`00baed18`](#insn-00baed18) 範囲 `[['00baed18', '00baed2f']]`
  - `FALL_THROUGH` [`00baed2c`](#insn-00baed2c) → [`00baed30`](#insn-00baed30)
- ブロック [`00baed30`](#insn-00baed30) 範囲 `[['00baed30', '00baed47']]`
  - `FALL_THROUGH` [`00baed44`](#insn-00baed44) → [`00baed48`](#insn-00baed48)
- ブロック [`00baed48`](#insn-00baed48) 範囲 `[['00baed48', '00baed57']]`
  - `FALL_THROUGH` [`00baed54`](#insn-00baed54) → [`00baed58`](#insn-00baed58)
- ブロック [`00baed58`](#insn-00baed58) 範囲 `[['00baed58', '00baed6b']]`

## 命令位置別の参照

- [`00baed04`](#insn-00baed04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed08`](#insn-00baed08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed30`](#insn-00baed30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed48`](#insn-00baed48) → [`00bae630`](00bae630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae630` · 推定シンボル `None` · 推定型 `None`
- [`00baed4c`](#insn-00baed4c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed58`](#insn-00baed58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed5c`](#insn-00baed5c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baed04`](#insn-00baed04)

~~~json
{
  "source": "00baed04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed08`](#insn-00baed08)

~~~json
{
  "source": "00baed08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed30`](#insn-00baed30)

~~~json
{
  "source": "00baed30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed48`](#insn-00baed48)

~~~json
{
  "source": "00baed48",
  "target": "00bae630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baed4c`](#insn-00baed4c)

~~~json
{
  "source": "00baed4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed58`](#insn-00baed58)

~~~json
{
  "source": "00baed58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed5c`](#insn-00baed5c)

~~~json
{
  "source": "00baed5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
