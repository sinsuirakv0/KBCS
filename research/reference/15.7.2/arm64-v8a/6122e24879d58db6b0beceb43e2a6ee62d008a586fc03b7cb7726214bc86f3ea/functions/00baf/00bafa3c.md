# 00bafa3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bafb04`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafb04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-513d6218c7607c411cfaa2d1b1de3527)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafa3c",
  "name": "_ZNSt6__ndk114__num_put_base14__format_floatEPcPKcj",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "169168058cacee446172326b7a20d3d42789a0d6794898bce7bd35b9a90166f1",
  "source_text_sha256": "169168058cacee446172326b7a20d3d42789a0d6794898bce7bd35b9a90166f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafa3c",
        "00bafaf3"
      ]
    ],
    "bytes_sha256": "ef4d67893758e19ea7d9b1fdc0e195f3d86a8af745e9436d5856a53e06229c56",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
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

## 疑似コード / UTF-8 1857 bytes

~~~c

bool _ZNSt6__ndk114__num_put_base14__format_floatEPcPKcj(char *param_1,char *param_2,uint param_3)

{
  uint uVar1;
  bool bVar2;
  char *pcVar3;
  char *pcVar4;
  char cVar5;
  char cVar6;
  
  pcVar3 = param_1;
  if ((param_3 >> 0xb & 1) != 0) {
    pcVar3 = param_1 + 1;
    *param_1 = '+';
  }
  pcVar4 = pcVar3;
  if ((param_3 >> 10 & 1) != 0) {
                    /* try { // try from 00bafa54 to 00cafaab has its CatchHandler @ 00bafa54
                       catch() { ... } // from try @ 00bafa54 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bafeec with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb01a0 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb051c with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb0924 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb0cdc with catch @ 00bafa54 */
    pcVar4 = pcVar3 + 1;
    *pcVar3 = '#';
  }
  uVar1 = param_3 & 0x104;
  pcVar3 = pcVar4;
  if (uVar1 != 0x104) {
    pcVar3 = pcVar4 + 2;
    pcVar4[0] = '.';
    pcVar4[1] = '*';
  }
  cVar6 = *param_2;
  while (cVar6 != '\0') {
    param_2 = param_2 + 1;
    *pcVar3 = cVar6;
    pcVar3 = pcVar3 + 1;
    cVar6 = *param_2;
  }
  if (uVar1 == 0x100) {
                    /* try { // try from 00bafaac to 00cafb0b has its CatchHandler @ 00bb0d0c */
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'E';
    cVar6 = 'e';
  }
  else if (uVar1 == 4) {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'F';
    cVar6 = 'f';
  }
  else if (uVar1 == 0x104) {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'A';
    cVar6 = 'a';
  }
  else {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'G';
    cVar6 = 'g';
  }
  if (!bVar2) {
    cVar6 = cVar5;
  }
  *pcVar3 = cVar6;
  return uVar1 != 0x104;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafa3c"></a> `00bafa3c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bafa40"></a> `00bafa40` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bafa44"></a> `00bafa44` | `62 00 58 36` | tbz w2,#0xb,0x00bafa50 | `CONDITIONAL_JUMP`
<a id="insn-00bafa48"></a> `00bafa48` | `69 05 80 52` | mov w9,#0x2b | `FALL_THROUGH`
<a id="insn-00bafa4c"></a> `00bafa4c` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafa50"></a> `00bafa50` | `62 00 50 36` | tbz w2,#0xa,0x00bafa5c | `CONDITIONAL_JUMP`
<a id="insn-00bafa54"></a> `00bafa54` | `69 04 80 52` | mov w9,#0x23 | `FALL_THROUGH`
<a id="insn-00bafa58"></a> `00bafa58` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafa5c"></a> `00bafa5c` | `89 20 80 52` | mov w9,#0x104 | `FALL_THROUGH`
<a id="insn-00bafa60"></a> `00bafa60` | `49 00 09 0a` | and w9,w2,w9 | `FALL_THROUGH`
<a id="insn-00bafa64"></a> `00bafa64` | `3f 11 04 71` | cmp w9,#0x104 | `FALL_THROUGH`
<a id="insn-00bafa68"></a> `00bafa68` | `60 00 00 54` | b.eq 0x00bafa74 | `CONDITIONAL_JUMP`
<a id="insn-00bafa6c"></a> `00bafa6c` | `ca 45 85 52` | mov w10,#0x2a2e | `FALL_THROUGH`
<a id="insn-00bafa70"></a> `00bafa70` | `0a 25 00 78` | strh w10,[x8], #0x2 | `FALL_THROUGH`
<a id="insn-00bafa74"></a> `00bafa74` | `2a 00 40 39` | ldrb w10,[x1] | `FALL_THROUGH`
<a id="insn-00bafa78"></a> `00bafa78` | `aa 00 00 34` | cbz w10,0x00bafa8c | `CONDITIONAL_JUMP`
<a id="insn-00bafa7c"></a> `00bafa7c` | `2b 04 00 91` | add x11,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00bafa80"></a> `00bafa80` | `0a 15 00 38` | strb w10,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bafa84"></a> `00bafa84` | `6a 15 40 38` | ldrb w10,[x11], #0x1 | `FALL_THROUGH`
<a id="insn-00bafa88"></a> `00bafa88` | `ca ff ff 35` | cbnz w10,0x00bafa80 | `CONDITIONAL_JUMP`
<a id="insn-00bafa8c"></a> `00bafa8c` | `3f 01 04 71` | cmp w9,#0x100 | `FALL_THROUGH`
<a id="insn-00bafa90"></a> `00bafa90` | `e0 00 00 54` | b.eq 0x00bafaac | `CONDITIONAL_JUMP`
<a id="insn-00bafa94"></a> `00bafa94` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bafa98"></a> `00bafa98` | `21 01 00 54` | b.ne 0x00bafabc | `CONDITIONAL_JUMP`
<a id="insn-00bafa9c"></a> `00bafa9c` | `5f 00 12 72` | tst w2,#0x4000 | `FALL_THROUGH`
<a id="insn-00bafaa0"></a> `00bafaa0` | `ca 08 80 52` | mov w10,#0x46 | `FALL_THROUGH`
<a id="insn-00bafaa4"></a> `00bafaa4` | `cb 0c 80 52` | mov w11,#0x66 | `FALL_THROUGH`
<a id="insn-00bafaa8"></a> `00bafaa8` | `0e 00 00 14` | b 0x00bafae0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafaac"></a> `00bafaac` | `5f 00 12 72` | tst w2,#0x4000 | `FALL_THROUGH`
<a id="insn-00bafab0"></a> `00bafab0` | `aa 08 80 52` | mov w10,#0x45 | `FALL_THROUGH`
<a id="insn-00bafab4"></a> `00bafab4` | `ab 0c 80 52` | mov w11,#0x65 | `FALL_THROUGH`
<a id="insn-00bafab8"></a> `00bafab8` | `0a 00 00 14` | b 0x00bafae0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafabc"></a> `00bafabc` | `3f 11 04 71` | cmp w9,#0x104 | `FALL_THROUGH`
<a id="insn-00bafac0"></a> `00bafac0` | `a0 00 00 54` | b.eq 0x00bafad4 | `CONDITIONAL_JUMP`
<a id="insn-00bafac4"></a> `00bafac4` | `5f 00 12 72` | tst w2,#0x4000 | `FALL_THROUGH`
<a id="insn-00bafac8"></a> `00bafac8` | `ea 08 80 52` | mov w10,#0x47 | `FALL_THROUGH`
<a id="insn-00bafacc"></a> `00bafacc` | `eb 0c 80 52` | mov w11,#0x67 | `FALL_THROUGH`
<a id="insn-00bafad0"></a> `00bafad0` | `04 00 00 14` | b 0x00bafae0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafad4"></a> `00bafad4` | `5f 00 12 72` | tst w2,#0x4000 | `FALL_THROUGH`
<a id="insn-00bafad8"></a> `00bafad8` | `2a 08 80 52` | mov w10,#0x41 | `FALL_THROUGH`
<a id="insn-00bafadc"></a> `00bafadc` | `2b 0c 80 52` | mov w11,#0x61 | `FALL_THROUGH`
<a id="insn-00bafae0"></a> `00bafae0` | `6a 01 8a 1a` | csel w10,w11,w10,eq | `FALL_THROUGH`
<a id="insn-00bafae4"></a> `00bafae4` | `3f 11 04 71` | cmp w9,#0x104 | `FALL_THROUGH`
<a id="insn-00bafae8"></a> `00bafae8` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bafaec"></a> `00bafaec` | `0a 01 00 39` | strb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bafaf0"></a> `00bafaf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafa3c`](#insn-00bafa3c) 範囲 `[['00bafa3c', '00bafa47']]`
  - `CONDITIONAL_JUMP` [`00bafa44`](#insn-00bafa44) → [`00bafa50`](#insn-00bafa50)
  - `FALL_THROUGH` [`00bafa44`](#insn-00bafa44) → [`00bafa48`](#insn-00bafa48)
- ブロック [`00bafa48`](#insn-00bafa48) 範囲 `[['00bafa48', '00bafa4f']]`
  - `FALL_THROUGH` [`00bafa4c`](#insn-00bafa4c) → [`00bafa50`](#insn-00bafa50)
- ブロック [`00bafa50`](#insn-00bafa50) 範囲 `[['00bafa50', '00bafa53']]`
  - `CONDITIONAL_JUMP` [`00bafa50`](#insn-00bafa50) → [`00bafa5c`](#insn-00bafa5c)
  - `FALL_THROUGH` [`00bafa50`](#insn-00bafa50) → [`00bafa54`](#insn-00bafa54)
- ブロック [`00bafa54`](#insn-00bafa54) 範囲 `[['00bafa54', '00bafa5b']]`
  - `FALL_THROUGH` [`00bafa58`](#insn-00bafa58) → [`00bafa5c`](#insn-00bafa5c)
- ブロック [`00bafa5c`](#insn-00bafa5c) 範囲 `[['00bafa5c', '00bafa6b']]`
  - `CONDITIONAL_JUMP` [`00bafa68`](#insn-00bafa68) → [`00bafa74`](#insn-00bafa74)
  - `FALL_THROUGH` [`00bafa68`](#insn-00bafa68) → [`00bafa6c`](#insn-00bafa6c)
- ブロック [`00bafa6c`](#insn-00bafa6c) 範囲 `[['00bafa6c', '00bafa73']]`
  - `FALL_THROUGH` [`00bafa70`](#insn-00bafa70) → [`00bafa74`](#insn-00bafa74)
- ブロック [`00bafa74`](#insn-00bafa74) 範囲 `[['00bafa74', '00bafa7b']]`
  - `CONDITIONAL_JUMP` [`00bafa78`](#insn-00bafa78) → [`00bafa8c`](#insn-00bafa8c)
  - `FALL_THROUGH` [`00bafa78`](#insn-00bafa78) → [`00bafa7c`](#insn-00bafa7c)
- ブロック [`00bafa7c`](#insn-00bafa7c) 範囲 `[['00bafa7c', '00bafa7f']]`
  - `FALL_THROUGH` [`00bafa7c`](#insn-00bafa7c) → [`00bafa80`](#insn-00bafa80)
- ブロック [`00bafa80`](#insn-00bafa80) 範囲 `[['00bafa80', '00bafa8b']]`
  - `CONDITIONAL_JUMP` [`00bafa88`](#insn-00bafa88) → [`00bafa80`](#insn-00bafa80)
  - `FALL_THROUGH` [`00bafa88`](#insn-00bafa88) → [`00bafa8c`](#insn-00bafa8c)
- ブロック [`00bafa8c`](#insn-00bafa8c) 範囲 `[['00bafa8c', '00bafa93']]`
  - `CONDITIONAL_JUMP` [`00bafa90`](#insn-00bafa90) → [`00bafaac`](#insn-00bafaac)
  - `FALL_THROUGH` [`00bafa90`](#insn-00bafa90) → [`00bafa94`](#insn-00bafa94)
- ブロック [`00bafa94`](#insn-00bafa94) 範囲 `[['00bafa94', '00bafa9b']]`
  - `CONDITIONAL_JUMP` [`00bafa98`](#insn-00bafa98) → [`00bafabc`](#insn-00bafabc)
  - `FALL_THROUGH` [`00bafa98`](#insn-00bafa98) → [`00bafa9c`](#insn-00bafa9c)
- ブロック [`00bafa9c`](#insn-00bafa9c) 範囲 `[['00bafa9c', '00bafaab']]`
  - `UNCONDITIONAL_JUMP` [`00bafaa8`](#insn-00bafaa8) → [`00bafae0`](#insn-00bafae0)
- ブロック [`00bafaac`](#insn-00bafaac) 範囲 `[['00bafaac', '00bafabb']]`
  - `UNCONDITIONAL_JUMP` [`00bafab8`](#insn-00bafab8) → [`00bafae0`](#insn-00bafae0)
- ブロック [`00bafabc`](#insn-00bafabc) 範囲 `[['00bafabc', '00bafac3']]`
  - `CONDITIONAL_JUMP` [`00bafac0`](#insn-00bafac0) → [`00bafad4`](#insn-00bafad4)
  - `FALL_THROUGH` [`00bafac0`](#insn-00bafac0) → [`00bafac4`](#insn-00bafac4)
- ブロック [`00bafac4`](#insn-00bafac4) 範囲 `[['00bafac4', '00bafad3']]`
  - `UNCONDITIONAL_JUMP` [`00bafad0`](#insn-00bafad0) → [`00bafae0`](#insn-00bafae0)
- ブロック [`00bafad4`](#insn-00bafad4) 範囲 `[['00bafad4', '00bafadf']]`
  - `FALL_THROUGH` [`00bafadc`](#insn-00bafadc) → [`00bafae0`](#insn-00bafae0)
- ブロック [`00bafae0`](#insn-00bafae0) 範囲 `[['00bafae0', '00bafaf3']]`

## 命令位置別の参照

- [`00bafa44`](#insn-00bafa44) → [`00bafa50`](#insn-00bafa50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa50`](#insn-00bafa50) → [`00bafa5c`](#insn-00bafa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa68`](#insn-00bafa68) → [`00bafa74`](#insn-00bafa74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa78`](#insn-00bafa78) → [`00bafa8c`](#insn-00bafa8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa88`](#insn-00bafa88) → [`00bafa80`](#insn-00bafa80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa90`](#insn-00bafa90) → [`00bafaac`](#insn-00bafaac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa98`](#insn-00bafa98) → [`00bafabc`](#insn-00bafabc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafaa8`](#insn-00bafaa8) → [`00bafae0`](#insn-00bafae0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafab8`](#insn-00bafab8) → [`00bafae0`](#insn-00bafae0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafac0`](#insn-00bafac0) → [`00bafad4`](#insn-00bafad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafad0`](#insn-00bafad0) → [`00bafae0`](#insn-00bafae0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafa44`](#insn-00bafa44)

~~~json
{
  "source": "00bafa44",
  "target": "00bafa50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa50`](#insn-00bafa50)

~~~json
{
  "source": "00bafa50",
  "target": "00bafa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa68`](#insn-00bafa68)

~~~json
{
  "source": "00bafa68",
  "target": "00bafa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa78`](#insn-00bafa78)

~~~json
{
  "source": "00bafa78",
  "target": "00bafa8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa88`](#insn-00bafa88)

~~~json
{
  "source": "00bafa88",
  "target": "00bafa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa90`](#insn-00bafa90)

~~~json
{
  "source": "00bafa90",
  "target": "00bafaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa98`](#insn-00bafa98)

~~~json
{
  "source": "00bafa98",
  "target": "00bafabc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafaa8`](#insn-00bafaa8)

~~~json
{
  "source": "00bafaa8",
  "target": "00bafae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafab8`](#insn-00bafab8)

~~~json
{
  "source": "00bafab8",
  "target": "00bafae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafac0`](#insn-00bafac0)

~~~json
{
  "source": "00bafac0",
  "target": "00bafad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafad0`](#insn-00bafad0)

~~~json
{
  "source": "00bafad0",
  "target": "00bafae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
