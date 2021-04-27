<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:pr="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"
    xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
    
    <xsl:template match="pr:PcGts">
        <PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd">
            <xsl:copy-of select="pr:Metadata"/>
            <xsl:apply-templates select="pr:Page"/>
        </PcGts>
    </xsl:template>
    
    <xsl:template match="pr:Page">
        <xsl:element name="Page">
            <xsl:attribute name="imageFilename">
                <xsl:value-of select="@imageFilename"/>
            </xsl:attribute>
            <xsl:attribute name="imageWidth">
                <xsl:value-of select="@imageWidth"/>
            </xsl:attribute>
            <xsl:attribute name="imageHeight">
                <xsl:value-of select="@imageHeight"/>
            </xsl:attribute>
            <xsl:apply-templates select="pr:TextRegion"/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="pr:TextRegion">
        <xsl:element name="TextRegion">
            <xsl:attribute name="id">
                <xsl:value-of select="@id"/>
            </xsl:attribute>
            <xsl:attribute name="custom">
                <xsl:value-of select="@custom"/>
            </xsl:attribute>
            <xsl:copy-of select="pr:Coords"/>
            <xsl:apply-templates select="pr:TextLine"/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="pr:TextLine">
        <xsl:element name="TextLine">
            <xsl:attribute name="id">
                <xsl:value-of select="@id"/>
            </xsl:attribute>
            <xsl:attribute name="custom">
                <xsl:value-of select="@custom"/>
            </xsl:attribute>
            <xsl:copy-of select="pr:Coords"/>
            <xsl:copy-of select="pr:Baseline"/></xsl:element>
    </xsl:template>
</xsl:stylesheet>
