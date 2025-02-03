import React from "react";

import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
	ErrorBoundary,
	SearchProvider,
	SearchBox,
	Results,
	PagingInfo,
	ResultsPerPage,
	Paging,
	WithSearch
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";
import 'dotenv/config';

const connector = new ElasticsearchAPIConnector({
	host: process.env.ELASTICSEARCH_URL || "http://localhost:9200",
	index: "cv-transcriptions",
});
const config = {
	searchQuery: {
		result_fields: {
			generated_text: {
				snippet: {
          size: 100,
          fallback: true
				},
			},
			durations: {
				snippet: {
          size: 100,
          fallback: true
				},
			},
			age: {
				snippet: {
					size: 100,
          fallback: true
				},
			},
			gender: {
				snippet: {
          size: 100,
          fallback: true
				},
			},
			accent: {
				snippet: {
          size: 100,
          fallback: true
				},
			},
		},
	},
	autocompleteQuery: {
		results: {
			resultsPerPage: 5,
			result_fields: {
				generated_text: {
					snippet: {
						size: 100,
						fallback: true
					},
				},
			}
		},
	},
	apiConnector: connector,
	alwaysSearchOnInitialLoad: true
};

export default function App() {
	return (
		<SearchProvider config={config}>
			<WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
				{({ wasSearched }) => {
					return (
						<div className="App">
							<ErrorBoundary>
								<Layout
									header={<SearchBox
										autocompleteMinimumCharacters={3}
										autocompleteResults={{
											linkTarget: "_blank",
											sectionTitle: "Results",
											titleField: "generated_text",
											urlField: "url",
											shouldTrackClickThrough: true
										}}
										autocompleteSuggestions={true}
										debounceLength={0}
									/>}
									bodyContent={
										<Results shouldTrackClickThrough={true}
										/>
									}
									bodyHeader={
										<React.Fragment>
											{wasSearched && <PagingInfo />}
											{wasSearched && <ResultsPerPage />}
										</React.Fragment>
									}
									bodyFooter={<Paging />}
								/>
							</ErrorBoundary>
						</div>
					);
				}}
			</WithSearch>
		</SearchProvider>
	);
}
